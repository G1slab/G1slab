#!/home/jaesoon/miniconda3/bin/python

import sys
import pysam
import cyvcf2

in_file_fa = sys.argv[1]
in_file_bam = sys.argv[2]
in_file_chrpos = sys.argv[3]

fasta = pysam.FastaFile(in_file_fa)

bam = pysam.AlignmentFile(in_file_bam)

with open(in_file_chrpos) as new_chrompos:
	new_chrompos=new_chrompos.read().splitlines()

new_chrompos_final = []

for z in new_chrompos:
	new_chrompos_final.append(eval(z))


def sequence_read(a, b):               #find reads in specific site + mapping quality
	list0 = []
	for pileupcolumn in bam.pileup(a, b-1, b, truncate = True, ignore_orphans = False, flag_filter = 1536, min_base_quality = 0): #ignore_orphans => count colorful reads too #stepper = nofileter => no extra filtering for reads #min_base_quality => why so many options??															 
		for pileupread in pileupcolumn.pileups:
			if not pileupread.is_del and not pileupread.is_refskip:
				list0.append((pileupread.alignment.query_name, pileupread.alignment.query_sequence[pileupread.query_position], pileupread.alignment.query_qualities[pileupread.query_position]))
	return list0                                                                                                                                                                                                                  ### not query_alignment_qualities!!!!!!!!#####

#for l in range(len(chrompos)):
#	print(sequence_read(chrompos[l][0], chrompos[l][1]))

def result(x, y):
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
		return str((x,y)) +  "\t"  + "Zero"

	altreads_BQ = [str(altreads[i][2]) for i in range(len(altreads))]

	return str((x,y)) +  "\t"  +  str(altreads_BQ.count("37")  +  altreads_BQ.count("74")*2  +  altreads_BQ.count("62") + altreads_BQ.count("48"))


for l in range(len(new_chrompos_final)):
	print(result(str(new_chrompos_final[l][0]), int(new_chrompos_final[l][1]))) #chrompos is fixed not chrompos[l]



















