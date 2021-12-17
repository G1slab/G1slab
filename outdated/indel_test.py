#!/home/jaesoon/miniconda3/bin/python

import sys
import cyvcf2
import pysam

fa = sys.argv[1]
fasta = pysam.FastaFile(fa)

infile_path_bam = sys.argv[2]
input_chr = str(sys.argv[3])
input_pos = int(sys.argv[4])

bam = pysam.AlignmentFile(infile_path_bam)

def VAFcal(bam, tup):
	global base
	ref =fasta.fetch(tup[0],tup[1]-1,tup[1])
	for pcol in bam.pileup(tup[0],tup[1]-1,tup[1], truncate = True):
		for pileupread in pcol.pileups:
			base = pcol.get_query_sequences(mark_matches = True, mark_ends = True, add_indels = True)
	list1 = [ref, ref.lower()]
	list2 = []
	for i in range(len(base)):
		if base[i] not in list1:
			 list2.append(base[i])
	return str(round(len(list2)/len(base), 3)) + "\t" + str(list1)

print(VAFcal(bam, (input_chr, input_pos)))
