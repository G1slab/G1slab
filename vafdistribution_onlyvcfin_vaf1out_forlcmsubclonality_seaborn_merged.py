#!/home/jaesoon/miniconda3/bin/python

import sys
import cyvcf2
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

infile_path = sys.argv[1]


with open(infile_path) as f:
	f=f.read().splitlines()

def plot_make(x):
	for i in range(len(x)):
		vcf_object = cyvcf2.VCF(x[i])
		variant_list = list(vcf_object)
		data1=[]
		for i in range(len(variant_list)):
			if (variant_list[i].gt_alt_freqs[0]) != 1.0:
				data1.append(variant_list[i].gt_alt_freqs[0])

		matplotlib.use("Agg")
		sns.kdeplot(data= data1,shade=True)

plot_make(f)
plt.savefig(f"{sys.argv[1]}.sns.png",dpi=300)


	

