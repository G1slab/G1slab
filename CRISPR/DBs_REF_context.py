#!/home/jaesoon/miniconda3/bin/python

import sys
import pysam
import cyvcf2

in_file_chrpos = sys.argv[1]
in_file_fasta = sys.argv[2]

fasta = pysam.FastaFile(in_file_fasta)

with open(in_file_chrpos) as new_chrompos:
    new_chrompos=new_chrompos.read().splitlines()

new_chrompos_final = []

for z in new_chrompos:
    new_chrompos_final.append(eval(z))

def final_maker(a, b, ls):
    ref_seq = fasta.fetch(a, b-41, b+40)
    
    seq_list = list(ref_seq)

    seq_list[int((len(seq_list)-1)/2)] = '{' + seq_list[int((len(seq_list)-1)/2)] + '}'

    return str((a, b)) + '\t' + str(seq_list)

for a in range(len(new_chrompos_final)):
    print(final_maker(new_chrompos_final[a][0], new_chrompos_final[a][1], new_chrompos_final))




