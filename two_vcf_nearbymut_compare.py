#!/home/jaesoon/miniconda3/bin/python

import sys
import pysam
import cyvcf2

in_file_vcf_1 = sys.argv[1]
in_file_vcf_2 = sys.argv[2]

vcf_object_1 = cyvcf2.VCF(in_file_vcf_1)
variant_list_1 = list(vcf_object_1)
vcf_object_2 = cyvcf2.VCF(in_file_vcf_2)
variant_list_2 = list(vcf_object_2)


chrompos_1 = []
chrompos_2 = []

for i in range(len(variant_list_1)):
	chrompos_1.append((variant_list_1[i].CHROM, variant_list_1[i].POS, variant_list_1[i].ALT[0]))

for j in range(len(variant_list_2)):
	chrompos_2.append((variant_list_2[j].CHROM, variant_list_2[j].POS, variant_list_2[j].ALT[0]))


#print(chrompos_1[0:10])
#print(chrompos_2[0:10])

param_range = int(sys.argv[3])

#for l in range(len(chrompos_1)):
#	if chrompos_1[l][0] == chrompos_2[m][0] and chrompos_1[l][2] == chrompos_2[m][2]:
#		if abs(chrompos_1[l][1] - chrompos_2[m][1]) < param_range:
#			print(str(chrompos_2[m]) + "same")
#		else:
#			print(str(chrompos_2[m])+"no")
#		m += 1
#	if m == len(chrompos_2):
#		break


for l in range(len(chrompos_1)):
	for m in range(len(chrompos_2)):
		if chrompos_1[l][0] == chrompos_2[m][0] and chrompos_1[l][2] == chrompos_2[m][2]:
			if abs(chrompos_1[l][1] - chrompos_2[m][1]) < param_range:
				print(str(chrompos_2[m]) + "sameexist")
			else:
				print(str(chrompos_2[m]) + "noneexist")	
