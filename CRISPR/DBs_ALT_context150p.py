#!/home/jaesoon/miniconda3/bin/python

import sys
import pysam
import cyvcf2

in_file_chrpos = sys.argv[1]
in_file_fasta = sys.argv[2]
in_file_bam = sys.argv[3]

bam = pysam.AlignmentFile(in_file_bam)
fasta = pysam.FastaFile(in_file_fasta)

with open(in_file_chrpos) as new_chrompos:
    new_chrompos=new_chrompos.read().splitlines()

new_chrompos_final = []

for z in new_chrompos:
    new_chrompos_final.append(eval(z))

#above makes [(chr,pos),(chr1,pos1),(chr2,pos2)]

def sequence_read(a, b):  
    list0 = []
    for pileupcolumn in bam.pileup(a, b-1, b, truncate = True, ignore_orphans = False, flag_filter = 1536, min_base_quality = 0): #ignore_orphans => count colorful reads too #stepper = nofileter => no extra filtering for reads #min_base_quality => why so many options??															 
        for pileupread in pileupcolumn.pileups:
            if not pileupread.is_del and not pileupread.is_refskip:
                list0.append(pileupread.alignment.query_sequence[pileupread.query_position])
    return list0

def sequence_final_decision(a, b, ls): #hwackjeong sequence of the loci
    ref = []
    alt = []
    ref_seq = fasta.fetch(a, b-1, b)  #ref context maybe extracted very easily
    for i in range(len(ls)):
        if ls[i] == ref_seq:
            ref.append(ls[i])
        else:
            alt.append(ls[i])
    if len(ref) + len(alt) < 4: #if depth is too low, just return ref
        return ref_seq
    if len(alt)/(len(alt) + len(ref)) > 0.9:     #if alt percentage is too high 
        return max(alt, key = alt.count) + '_hom' #-> homo mutation.
    if len(ref) >= 4 and len(alt) > 2:
        return max(alt, key = alt.count) #for the multiallele, choose most common appearance as alt
    if len (ref) >= 4 and len(alt) <= 2: #if alt read is not sufficient, just return ref
        return ref_seq

def final_maker(ls1): #input -> [(chr,pos)......] 
    seq_list = []

    for a in range(len(ls1)):
        seq_list.append(sequence_final_decision(ls1[a][0], ls1[a][1], sequence_read(ls1[a][0], ls1[a][1])))
    
    seq_list[int((len(seq_list)-1)/2)] = '{' + str(seq_list[int((len(seq_list)-1)/2)]) + '}' #make ALT or REF loci distinguishable #center str(seq~~) is needed
 
    return str((ls1[int((len(seq_list)-1)/2)][0], ls1[int((len(seq_list)-1)/2)][1]))  + "\t" + str(seq_list) #center is the input original loci

def context_out(tup, c): #make context of loci. +-Nbp  #output look like [[(),(),()],[(),(),()],[(),(),()]]
    l1 = []
    l2 = []
    for i in range(c):
        l1.append((tup[0], tup[1] - (c-i)))
    for a in range(c + 1):
        l2.append((tup[0], tup[1] + a))
    return l1 + l2

context_list = []

for k in range(len(new_chrompos_final)):
    context_list.append(context_out(new_chrompos_final[k], 150)) #10 is variable number
    
#print(context_list)

for z in range(len(context_list)):
    print(final_maker(context_list[z]))



