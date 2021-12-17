#!/home/jaesoon/miniconda3/bin/python

import pandas as pd
import numpy as np
import sys

M_list=sys.argv[1]

with open(M_list) as f:
	f=f.read().splitlines()

a=' bamsnap -ref /data/jaesoon/DB/gunhee/pig/before/Sscrefa11.1_rename/Sscrofa11.1_genomic.rename.fna -bam p_6390_s_bl_g2_10.s.md.ir.bam p_6392_s_bl_g2_11.s.md.ir.bam p_6393_s_bl_g2_12.s.md.ir.bam p_6394_s_bl_g2_13.s.md.ir.bam p_6395_s_bl_g2_14.s.md.ir.bam p_6396_s_bl_g2_15.s.md.ir.bam p_6397_s_bl_g2_16.s.md.ir.bam p_6057_f_bl_g2_9.s.md.ir.bam p_6073_m_bl_g2_1.s.md.ir.bam -show_soft_clipped -pos hi -out /data/jaesoon/DB/SG/bamsnap/pig/p_g2.merged.hi.png'

list1=[]

for i in range(len(f)):
	list1.append(a.replace('hi',f[i]))

for j in range(len(list1)):
	print(list1[j])
	

