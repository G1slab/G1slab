#!/home/jaesoon/miniconda3/bin/python

import pysam
import sys
import cyvcf2

fa = sys.argv[1]
fasta = pysam.FastaFile(fa)

in_file_bam = sys.argv[2]
bam = pysam.AlignmentFile(in_file_bam)

infile_path = sys.argv[3]

vcf_object = cyvcf2.VCF(infile_path)
variant_list = list(vcf_object)

chrompos = []	

for i in range(len(variant_list)):
	chrompos.append((variant_list[i].CHROM, variant_list[i].POS))

def sequence_read(a, b):               #find reads in specific site + mapping quality
	list0 = []
	for pileupcolumn in bam.pileup(a, b-1, b, truncate = True, ignore_orphans = False, stepper = 'nofilter', min_base_quality = 0): #ignore_orphans => count colorful reads too #stepper = nofileter => no extra filtering for reads #min_base_quality => why so many options??															 
		for pileupread in pileupcolumn.pileups:
			if not pileupread.is_del and not pileupread.is_refskip:
				list0.append((pileupread.alignment.query_name, pileupread.alignment.query_sequence[pileupread.query_position]))
	return list0

def altread_out(x, y):
	refalt = fasta.fetch(str(x),int(y)-1,int(y))
	basereads = sequence_read(str(x), int(y)) #basic read #list form

	refreads = [] #reads not containing variants
	altreads = [] #reads containing variants

	for k in range(len(basereads)):
		if basereads[k][1] == refalt:
			refreads.append(basereads[k])
		else:
			altreads.append(basereads[k])
	
	return [(x, int(y)), altreads] #position and altread info out


def two_list_compare(ls1, ls2):
	count = 0
	readid = []
	for i in range(len(ls1[1])):
		for j in range(len(ls2[1])):
			if ls1[1][i][0] == ls2[1][j][0]: #compare between read id , not base -> base can be different on the same read
				count +=1
				readid.append(ls1[1][i][0])
	return (len(ls1[1]), count, ls1[1][i][0], ls2[0]) # compare between two (chr pos alt read id) set, 
										 # len(ls1[1]0 -> for comparison, the counterpart mutations have to have similar number of mutations
									     ##maybe consider same?... because we dont want to drop true postives
										 ### same in N+ samples? -> ?? 2 or 3 same will definately be a false positive by nearby

def result(chrom, pos):
	mut_in_range = []

	for a in range(int(pos)-75, int(pos)+75):        #call every positions in range
		mut_in_range.append(altread_out(chrom, a))



	mut_in_range_filtered = []

											  
	for b in mut_in_range:
		if len(b[1]) != 0:
			mut_in_range_filtered.append(b) #append every chr pos alt read ID

	mut_in_range_filtered.remove(altread_out(chrom, pos)) #remove input itself


	candi = []
										 

	for c in range(len(mut_in_range_filtered)):
		candi.append(two_list_compare(altread_out(chrom, pos), mut_in_range_filtered[c]))


	exact = []
	one_diff = []

	for d in range(len(candi)):
		if candi[d][0] > 1:
			if abs(candi[d][0] - candi[d][1]) == 0:
				exact.append(candi[d])
			if abs(candi[d][0] - candi[d][1]) == 1:
				one_diff.append(candi[d])

	return ((chrom, pos), (len(exact), len(one_diff)))


for m in range(len(chrompos)):
	print(result(chrompos[m][0], chrompos[m][1]))
