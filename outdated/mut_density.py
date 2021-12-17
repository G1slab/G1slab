#!/home/jaesoon/miniconda3/bin/python

import sys

infile_path = f'/data/jaesoon/DB/gunhee/pig/WGRS-TBD190385-20210112/sam/s.md.bam/VCF/{sys.argv[1]}'

import cyvcf2

vcf_object = cyvcf2.VCF(infile_path)

variant_list = list(vcf_object)

data = []

for i in range(len(variant_list)):
	data.append((variant_list[i].CHROM, variant_list[i].POS))

print(len(data))

pos = []

for j in range(len(data)):
	if data[j][0] == f'{sys.argv[2]}':
		pos.append(data[j][1])

print(len(pos))


import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
 
plt.hist(data, bins=100) #make histogram with numbers in list
plt.savefig(f'{sys.argv[1]}.{sys.argv[2]}.jpg', dpi=300)


