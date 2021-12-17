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
	for pileupcolumn in bam.pileup(a, b-1, b, truncate = True, ignore_orphans = False, ignore_overlaps = False, stepper = "nofilter", min_base_quality = 0): #ignore_orphans => count colorful reads too #stepper = nofileter => no extra filtering for reads #min_base_quality => why so many options??															 
		for pileupread in pileupcolumn.pileups:
			if not pileupread.is_del and not pileupread.is_refskip:
				list0.append((pileupread.alignment.query_name, pileupread.alignment.query_sequence[pileupread.query_position], pileupread.alignment.mapping_quality, pileupread.alignment.get_cigar_stats()[0], pileupread.alignment.get_cigar_stats()[1], pileupread.alignment.get_tag('NM')))
	return list0
                                       #[0] in get_cigar_stats -> how many
	                                   #[1] in get_cigar_stats -> how many times appeared?
                                       #NM => number of mismatches total

def result(x, y, ls):
	global fasta
	refalt = fasta.fetch(str(x),int(y)-1,int(y))

	basereads = sequence_read(str(x), int(y)) #basic read #list form

	soft_clipped_sum = 0

	for d in range(len(basereads)):
		if basereads[d][3][4] > 0:
			soft_clipped_sum += 1
	

	percent_soft_clipped_sum = soft_clipped_sum/len(basereads)

	param6 = 0.3

	checker = 0

	if percent_soft_clipped_sum > param6:
		checker += 1

	if checker == 0:
		return str((x, y)) + str(len(basereads)) + str(basereads)
	else:
		return  str((x,y))  +  "None" + str(len(basereads)) + str(basereads)




for l in range(len(chrompos)):
	print(result(str(chrompos[l][0]), int(chrompos[l][1]), chrompos)) #chrompos is fixed not chrompos[l]




















