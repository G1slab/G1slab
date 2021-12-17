#!/home/jaesoon/miniconda3/bin/python

import sys
import cyvcf2
import pysam

fa = '/data/jaesoon/DB/gunhee/pig/before/Sscrefa11.1_rename/Sscrofa11.1_genomic.rename.fna'

fasta = pysam.FastaFile(fa)


infile_path_vcf = sys.argv[1] #merged vcf -> for variant list
infile_path_bam = sys.argv[2] #het parent bam -> for vaf output

bam = pysam.AlignmentFile(infile_path_bam)

vcf_object = cyvcf2.VCF(infile_path_vcf)

variant_list = list(vcf_object)

chrompos = [] 

for i in range(len(variant_list)):
	chrompos.append((variant_list[i].CHROM, variant_list[i].POS))

def VAFcal(bam, tup):
	global base
	ref =fasta.fetch(tup[0],tup[1]-1,tup[1])
	for pcol in bam.pileup(tup[0],tup[1]-1,tup[1], truncate = True):
		for pileupread in pcol.pileups:
			base = pcol.get_query_sequences()
	list1 = [ref, ref.lower()]
	list2 = []
	for i in range(len(base)):
		if base[i] not in list1:
			 list2.append(base[i])
	return round(len(list2)/len(base), 3)

data = []

for j in range(len(variant_list)):
	data.append(VAFcal(bam, chrompos[j]))

import matplotlib.pyplot as plt

plt.hist(data,bins=100)
plt.savefig(f"{sys.argv[1]}{sys.argv[2]}.png",dpi=300)
