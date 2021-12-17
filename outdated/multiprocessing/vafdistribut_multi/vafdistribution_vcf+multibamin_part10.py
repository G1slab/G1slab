#!/home/jaesoon/miniconda3/bin/python

import sys
import cyvcf2
import pysam
import numpy as np

fa = '/data/jaesoon/DB/Mouse_Raw/GRCm38.fa'
fasta = pysam.FastaFile(fa)


infile_path_vcf = sys.argv[1] #merged vcf -> for variant list
infile_path_bam1 = sys.argv[2] #het parent bam -> for vaf output
infile_path_bam2 = sys.argv[3] #het parent bam -> for vaf output
infile_path_bam3 = sys.argv[4] #het parent bam -> for vaf output
infile_path_bam4 = sys.argv[5] #het parent bam -> for vaf output
infile_path_bam5 = sys.argv[6] #het parent bam -> for vaf output
infile_path_bam6 = sys.argv[7] #het parent bam -> for vaf output
infile_path_bam7 = sys.argv[8] #het parent bam -> for vaf output
infile_path_bam8 = sys.argv[9] #het parent bam -> for vaf output
infile_path_bam9 = sys.argv[10] #het parent bam -> for vaf output
infile_path_bam10 = sys.argv[11] #het parent bam -> for vaf output

bam1 = pysam.AlignmentFile(infile_path_bam1)
bam2 = pysam.AlignmentFile(infile_path_bam2)
bam3 = pysam.AlignmentFile(infile_path_bam3)
bam4 = pysam.AlignmentFile(infile_path_bam4)
bam5 = pysam.AlignmentFile(infile_path_bam5)
bam6 = pysam.AlignmentFile(infile_path_bam6)
bam7 = pysam.AlignmentFile(infile_path_bam7)
bam8 = pysam.AlignmentFile(infile_path_bam8)
bam9 = pysam.AlignmentFile(infile_path_bam9)
bam10 = pysam.AlignmentFile(infile_path_bam10)

vcf_object = cyvcf2.VCF(infile_path_vcf)

variant_list = list(vcf_object)

chrompos = [] 

for i in range(len(variant_list)):
	chrompos.append((variant_list[i].CHROM, variant_list[i].POS))

def VAFcal(bam, tup):
	global base
	ref =fasta.fetch(tup[0],int(tup[1])-1,int(tup[1]))
	for pcol in bam.pileup(tup[0],int(tup[1])-1,int(tup[1]), truncate = True):
		for pileupread in pcol.pileups:
			base = pcol.get_query_sequences()
	list1 = [ref, ref.lower()]
	list2 = []
	for i in range(len(base)):
		if base[i] not in list1:
			 list2.append(base[i])
	return round(len(list2)/len(base), 3)

chrompos_array = np.array(chrompos)

chrompos_split = np.array_split(chrompos_array,  10)

chrompos_10 = chrompos_split[9]

for j in range(len(chrompos_10)):
	print(str(tuple(chrompos_10[j])) +  "\t"  + str(VAFcal(bam1, chrompos_10[j])) + "\t" + str(VAFcal(bam2, chrompos_10[j])) +"\t" + str(VAFcal(bam3, chrompos_10[j])) +"\t" + str(VAFcal(bam4, chrompos_10[j])) +"\t" + str(VAFcal(bam5, chrompos_10[j])) +"\t" + str(VAFcal(bam6, chrompos_10[j])) +"\t" + str(VAFcal(bam7, chrompos_10[j])) +"\t" + str(VAFcal(bam8, chrompos_10[j])) +"\t" + str(VAFcal(bam9, chrompos_10[j])) +"\t" + str(VAFcal(bam10, chrompos_10[j])))	