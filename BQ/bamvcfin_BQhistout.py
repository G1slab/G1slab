#!/home/jaesoon/miniconda3/bin/python

import sys
import pysam
import cyvcf2

in_file_fa = sys.argv[1]
in_file_bam = sys.argv[2]
in_file_vcf = sys.argv[3]

fasta = pysam.FastaFile(in_file_fa)

bam = pysam.AlignmentFile(in_file_bam)

vcf_object = cyvcf2.VCF(in_file_vcf)
variant_list = list(vcf_object)

chrompos = []

for i in range(len(variant_list)):
	chrompos.append((variant_list[i].CHROM, variant_list[i].POS, variant_list[i].REF, variant_list[i].ALT))


def sequence_read(a, b):               #find reads in specific site + mapping quality
	list0 = []
	for pileupcolumn in bam.pileup(a, b-1, b, truncate = True, ignore_orphans = False, stepper ='nofilter', min_base_quality = 0): #ignore_orphans => count colorful reads too #stepper = nofileter => no extra filtering for reads #min_base_quality => why so many options??															 
		for pileupread in pileupcolumn.pileups:
			if not pileupread.is_del and not pileupread.is_refskip:
#list0.append((pileupread.alignment.query_name, pileupread.alignment.query_sequence[pileupread.query_position]))
				list0.append((pileupread.alignment.query_name, pileupread.alignment.query_sequence[pileupread.query_position], pileupread.alignment.query_qualities[pileupread.query_position]))
	return list0                                                                                                                                                                                                                  ### not query_alignment_qualities!!!!!!!!#####

#for l in range(len(chrompos)):
#	print(sequence_read(chrompos[l][0], chrompos[l][1]))

def result(x, y, ls):
	global fasta
	refalt = fasta.fetch(str(x),int(y)-1,int(y))

	basereads = sequence_read(str(x), int(y)) #basic read #list form

	refreads = [] #reads not containing variants
	altreads = [] #reads containing variants

	for k in range(len(basereads)):
		if basereads[k][1] == refalt:
			refreads.append(basereads[k])
		else:
			altreads.append(basereads[k])

	if len(altreads) == 0:
		return None

	altreads_BQ = [altreads[i][2] for i in range(len(altreads))]

	return sum(altreads_BQ)/len(altreads_BQ)

data = []

for l in range(len(chrompos)):
	data.append(result(str(chrompos[l][0]), int(chrompos[l][1]), chrompos)) #chrompos is fixed not chrompos[l]

import matplotlib.pyplot as plt

plt.hist(data,bins=100)
plt.savefig(f"{sys.argv[3]}BQmean.png",dpi=300)




















