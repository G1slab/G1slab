#!/home/jaesoon/miniconda2/bin/python
#import numpy #while bringing cyvcf2, it is automatically imported

import sys

#sys.path.append("/home/jaesoon/miniconda3/lib/python3.8/site-packages") -> while using conda, no need

infile_path = sys.argv[1]

import cyvcf2
vcf_object = cyvcf2.VCF(infile_path)
variant_list = list(vcf_object)

data=[]
for i in range(len(variant_list)):
	if (variant_list[i].gt_alt_freqs[0]) != 1.0:
		data.append(variant_list[i].gt_alt_freqs[0])

import matplotlib.pyplot as plt

plt.hist(data,bins=100)
plt.savefig(f"{sys.argv[1]}.png",dpi=300)
