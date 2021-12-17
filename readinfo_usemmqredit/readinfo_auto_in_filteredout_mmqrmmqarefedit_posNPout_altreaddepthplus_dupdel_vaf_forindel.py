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


#print(chrompos[0:10])


def sequence_read(a, b):               #find reads in specific site + mapping quality
	list0 = []
	for pileupcolumn in bam.pileup(a, b-1, b, truncate = True, ignore_orphans = False, flag_filter = 1536, min_base_quality = 0): #ignore_orphans => count colorful reads too #stepper = nofileter => no extra filtering for reads #min_base_quality => why so many options??															 
		for pileupread in pileupcolumn.pileups:
			if not pileupread.is_del and not pileupread.is_refskip:
				list0.append((pileupread.alignment.query_name, pileupread.alignment.query_sequence[pileupread.query_position], pileupread.alignment.mapping_quality, pileupread.alignment.get_cigar_stats()[0], pileupread.alignment.get_cigar_stats()[1], pileupread.alignment.get_tag('NM'),  pileupcolumn.get_query_sequences(mark_matches = True, mark_ends = True, add_indels = True)))
	return list0
                                       #[0] in get_cigar_stats -> how many
	                                   #[1] in get_cigar_stats -> how many times appeared?
                                       #NM => number of mismatches total

def new_seqmaker(ls):         #for outputs in sequence_read(), make outputs with indel sequences (without this, ls[i][6] will be whole sequences for all readids)
  for i in range(len(ls)):
    ls[i]= list(ls[i])
    ls[i][6] = ls[i][6][i]
  return ls

def indel_expression(ls):  #given refalt from cycvf2, makes outputs same form as in new_seqmaker(), ex -> G+2AA, t-1nnn
  if len(ls[0]) < len(ls[1]):
    return [str(str(ls[0]) + "+" + str(len(ls[1])-1) + str(ls[1][1:])), str(str(ls[0]) + "+" + str(len(ls[1])-1) + str(ls[1][1:])).lower()]
  else:
    return [str(str(ls[1]) + "-" + str(len(ls[0])-1)+"N"*(len(ls[0])-1)), str(str(ls[1]) + "-" + str(len(ls[0])-1)+"N"*(len(ls[0])-1)).lower()]


def altcountdepth_indel(x, y):
	basereads = sequence_read(str(x), int(y))

	refreads = [] #reads not containing variants
	altreads = [] #reads containing variants

	refalt =  []
	for i in range(len(chrompos)):                                                       #get refalt from cyvcf2 -> because from cyvcf, indel refalt is correct
		if chrompos[i][0] == str(x) and chrompos[i][1] == int(y):
			refalt.append(chrompos[i][2])
			refalt.append(chrompos[i][3][0])

	alt = indel_expression(refalt) #main
	new_basereads = new_seqmaker(basereads)#main

	for k in range(len(new_basereads)):
		if new_basereads[k][-1]  in alt:
			altreads.append(new_basereads[k])
		else:
			refreads.append(new_basereads[k])
	

	if len(altreads) == 0:
		return str((x, y)) + "\t" + str([len(altreads), len(basereads)]) +  "_" + "Zero" + " " + str(len(altreads))

	ref_mappingQ_sum = 0

	for a in range(len(refreads)):
		ref_mappingQ_sum += refreads[a][2]

	alt_mappingQ_sum = 0

	for b in range(len(altreads)):
		alt_mappingQ_sum += altreads[b][2]

	alt_mismatch_sum = 0

	for c in range(len(altreads)):
		alt_mismatch_sum += altreads[c][-2] #### -1  ->  -2 because one element is added to the end of altread#####

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




	param1 = 3
	param2 = 10
	param3 = 40
	param4 = 40
	param5 = 5
	param6 = 0.9

	checker = 0

	if supporting_reads_num < param1:
		checker += 1
	if mean_mappingQ_refreads - mean_mappingQ_altreads > param2:
		checker += 1
	if mean_mappingQ_altreads < param3:
		checker += 1
	if mean_mappingQ_refreads < param4:
		checker += 1
	if mean_mismatch_altreads > param5:
		checker += 1
	if percent_soft_clipped_sum > param6:
		checker += 1


	if checker == 0:
		return str((x, y)) + "\t" + str([len(altreads), len(basereads)]) +  "_" + "P" + " "+str(round(len(altreads)/len(basereads), 3))
	else:
		return str((x, y)) + "\t" + str([len(altreads), len(basereads)]) +  "_" + "N" + " "+str(round(len(altreads)/len(basereads), 3))



for l in range(len(chrompos)):
	print(altcountdepth_indel(str(chrompos[l][0]), int(chrompos[l][1]))) #chrompos is fixed not chrompos[l]






#return str((x,y)) + "\t" + str([len(altreads), len(basereads)]) + "\t" + str(refalt)


#for l in range(len(chrompos)):
#	print(altcountdepth_indel(str(chrompos[l][0]), int(chrompos[l][1])))









