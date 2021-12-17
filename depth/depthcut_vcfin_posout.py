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
	for pileupcolumn in bam.pileup(a, b-1, b, truncate = True, ignore_orphans = False, stepper = 'nofilter', min_base_quality = 0): #ignore_orphans => count colorful reads too #stepper = nofileter => no extra filtering for reads #min_base_quality => why so many options??															 
		for pileupread in pileupcolumn.pileups:
			if not pileupread.is_del and not pileupread.is_refskip:
				list0.append((pileupread.alignment.query_name, pileupread.alignment.query_sequence[pileupread.query_position], pileupread.alignment.mapping_quality, pileupread.alignment.get_cigar_stats()[0], pileupread.alignment.get_cigar_stats()[1], pileupread.alignment.get_tag('NM')))
	return list0
                                       #[0] in get_cigar_stats -> how many
	                                   #[1] in get_cigar_stats -> how many times appeared?
                                       #NM => number of mismatches total

def result(x, y, ls):	
	basereads = sequence_read(str(x), int(y)) #basic read #list form
	return len(basereads)
	

depth = sys.argv[4]

for l in range(len(chrompos)):
	if result(str(chrompos[l][0]), int(chrompos[l][1]), chrompos) < int(depth):
		print((str(chrompos[l][0]), int(chrompos[l][1])))
	else:
		print("None")


#data = []

#for l in range(len(chrompos)):
#	data.append(result(str(chrompos[l][0]), int(chrompos[l][1]), chrompos)) #chrompos is fixed not chrompos[l]

#import matplotlib.pyplot as plt

#plt.hist(data,bins=100)
#plt.savefig(f"{sys.argv[1]}{sys.argv[2]}.png",dpi=300)
