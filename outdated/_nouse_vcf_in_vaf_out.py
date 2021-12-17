#!/home/jaesoon/miniconda2/bin/python

import sys
import pysam

fa=sys.argv[1]
fasta=pysam.FastaFile(fa)

infile_path = sys.argv[3]

import cyvcf2
vcf_object = cyvcf2.VCF(infile_path)
variant_list = list(vcf_object)


chrompos=[]


for i in range(len(variant_list)):
	chrompos.append((variant_list[i].CHROM, variant_list[i].POS))
#print(chrompos[i])


infile_bam=sys.argv[2]

bam = pysam.AlignmentFile(infile_bam)	

def VAFcal(bam, tup):
	global based
	ref =fasta.fetch(tup[0],tup[1]-1,tup[1])
	for pcol in bam.pileup(tup[0],tup[1]-1,tup[1], truncate = True):
		for pileupread in pcol.pileups:
			based = pcol.get_query_sequences()
	list1 = [ref, ref.lower()]
	list2 = []
	for i in range(len(based)):
		if based[i] not in list1:
			 list2.append(based[i])
	return round(len(list2)/len(based), 3)

for j in range(len(variant_list)):	
	print(VAFcal(bam,(chrompos[j][0], chrompos[j][1])))

