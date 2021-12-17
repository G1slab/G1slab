#!/home/jaesoon/miniconda3/bin/python

import pandas as pd
import numpy as np
import sys

M_list=sys.argv[1]

with open(M_list) as f:
	f=f.read().splitlines()

for k in range(len(f)):
	f[k] = str(eval(f[k])[0]) + ":" +str(eval(f[k])[1]) #input can be ('chr', pos)

a= 'bamsnap -ref /data/jaesoon/DB/gunhee/pig/before/Sscrefa11.1_rename/Sscrofa11.1_genomic.rename.uppercase.converted.fna -bam pig_15L_LU2_8A.s.md.ir.bam pig_15L_RUS1_2_4G.s.md.ir.bam pig_15L_SHM3_2_8G.s.md.ir.bam pig_15R_EY4_1H.s.md.ir.bam pig_15R_LU11_1D.s.md.ir.bam pig_15R_RUS1_2_3B.s.md.ir.bam pig_15R_SHM3_4_1A.s.md.ir.bam -save_image_only -silence -show_soft_clipped -pos hi -out /data/jaesoon/DB/SG/bamsnap/p_15.merged.hi.png'
list1=[]

for i in range(len(f)):
	list1.append(a.replace('hi',f[i]))

for j in range(len(list1)):
	print(list1[j])
	

