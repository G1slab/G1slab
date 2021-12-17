#!/home/jaesoon/miniconda3/bin/python

import sys

infile_path = sys.argv[1]

import cyvcf2
vcf_object = cyvcf2.VCF(infile_path)
variant_list = list(vcf_object)

data1=[]
for i in range(len(variant_list)):
	if (variant_list[i].gt_alt_freqs[0]) != 1.0 and (variant_list[i].gt_alt_freqs[0]) > 0.1 and (variant_list[i].gt_alt_freqs[0]) < 0.9:
		data1.append(variant_list[i].gt_alt_freqs[0])

import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
matplotlib.use("Agg")

sns.kdeplot(data= data1,shade=True)
plt.savefig(f"{sys.argv[1]}.sns.png",dpi=300)
