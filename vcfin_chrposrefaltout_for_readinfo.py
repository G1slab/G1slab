#!/home/jaesoon/miniconda3/bin/python

import sys
import cyvcf2

in_file_vcf = sys.argv[1]

vcf_object = cyvcf2.VCF(in_file_vcf)
variant_list = list(vcf_object)

chrompos = []

for i in range(len(variant_list)):
	print((variant_list[i].CHROM, variant_list[i].POS, variant_list[i].REF, variant_list[i].ALT[0]))
