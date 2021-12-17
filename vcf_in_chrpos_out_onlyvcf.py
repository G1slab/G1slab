#!/home/jaesoon/miniconda2/bin/python

import sys

infile_path = sys.argv[1]

import cyvcf2
vcf_object = cyvcf2.VCF(infile_path)
variant_list = list(vcf_object)

for i in range(len(variant_list)):
	print((variant_list[i].CHROM, variant_list[i].POS))