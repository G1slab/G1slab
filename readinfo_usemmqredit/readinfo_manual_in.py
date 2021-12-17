#!/home/jaesoon/miniconda3/bin/python

import sys
import pysam
import cyvcf2

in_file_fa = '/data/jaesoon/DB/Mouse_Raw/GRCm38.fa'

in_file_bam = sys.argv[1]
in_file_vcf = sys.argv[2]

fasta = pysam.FastaFile(in_file_fa)

bam = pysam.AlignmentFile(in_file_bam)

vcf_object = cyvcf2.VCF(in_file_vcf)
variant_list = list(vcf_object)

chrompos = []

for i in range(len(variant_list)):
	chrompos.append((variant_list[i].CHROM, variant_list[i].POS, variant_list[i].REF, variant_list[i].ALT))


chrom = str(sys.argv[3])
pos = int(sys.argv[4])

print([chrom, pos])


def sequence_read(a, b):               #find reads in specific site + mapping quality
	list0 = []
	for pileupcolumn in bam.pileup(a, b-1, b, truncate = True, ignore_orphans = False, stepper = 'nofilter'): #ignore_orphans => count colorful reads too #stepper = nofileter => no extra filtering for reads															 
		for pileupread in pileupcolumn.pileups:
			if not pileupread.is_del and not pileupread.is_refskip:
				list0.append((pileupread.alignment.query_name, pileupread.alignment.query_sequence[pileupread.query_position], pileupread.alignment.mapping_quality, pileupread.alignment.get_cigar_stats()[0], pileupread.alignment.get_cigar_stats()[1], pileupread.alignment.get_tag('NM')))
	return list0
                                       #[0] in get_cigar_stats -> how many
	                                   #[1] in get_cigar_stats -> how many times appeared?
                        				#NM => number of mismatches total
refalt = [] 

for j in range(len(chrompos)):
	if chrompos[j][0] == chrom and chrompos[j][1] == pos:
		refalt.append(chrompos[j][2])
		refalt.append(chrompos[j][3][0])
	    #for alt, [0] is added to ignore mutlple alleles

if len(refalt) == 2:
	pass
else:
	sys.exit()


basereads = sequence_read(chrom, pos) #basic read #list form

refreads = [] #reads not containing variants
altreads = [] #reads containing variants

for k in range(len(basereads)):
	if basereads[k][1] == refalt[0]:
		refreads.append(basereads[k])
	else:
		altreads.append(basereads[k])

if len(altreads) == 0:
	sys.exit()

ref_mappingQ_sum = 0

for a in range(len(refreads)):
	ref_mappingQ_sum += refreads[a][2]


alt_mappingQ_sum = 0

for b in range(len(altreads)):
	alt_mappingQ_sum += altreads[b][2]

alt_mismatch_sum = 0

for c in range(len(altreads)):
	alt_mismatch_sum += altreads[c][-1]

soft_clipped_sum = 0

for d in range(len(altreads)):
	if altreads[d][3][4] > 0:
		soft_clipped_sum += 1
	


supporting_reads_num = len(altreads)
mean_mappingQ_altreads = alt_mappingQ_sum/len(altreads) 

if len(refreads) == 0:
	mean_mappingQ_refreads = 60
else:
	mean_mappingQ_refreads = ref_mappingQ_sum/len(refreads)

mean_mismatch_altreads = alt_mismatch_sum/len(altreads)
percent_soft_clipped_sum = soft_clipped_sum/len(altreads)



##############################################################################################
#param1 = 3
#param2 = 10
#param3 = 40
#param4 = 40
#param5 = 5
#param6 = 0.9
#
#checker = 0
#
#if supporting_reads_num < param1:
#	checker += 1
#if abs(mean_mappingQ_altreads - mean_mappingQ_refreads) > param2:
#	checker += 1
#if mean_mappingQ_altreads < param3:
#	checker += 1
#if mean_mappingQ_refreads < param4:
#	checker += 1
#if mean_mismatch_altreads > param5:
#	checker += 1
#if percent_soft_clipped_sum > param6:
#	checker += 1
#
#
#if checker == 0:
#	print((chrom, pos))
#
####################################################################################################





print("srn : " + str(supporting_reads_num))
print("mmqa : " + str(mean_mappingQ_altreads))
print("mmqr : " + str(mean_mappingQ_refreads))
print("absmqar : " + str(abs(mean_mappingQ_altreads - mean_mappingQ_refreads)))
print("mmisar : " + str(mean_mismatch_altreads))
print("psoft : " + str(percent_soft_clipped_sum))
print("")
























