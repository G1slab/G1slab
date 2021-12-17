#!/home/jaesoon/miniconda3/bin/python

import pandas as pd
import numpy as np
import sys

M_list=sys.argv[1]

with open(M_list) as f:
	f=f.read().splitlines()

for k in range(len(f)):
	f[k] = str(eval(f[k])[0]) + ":" +str(eval(f[k])[1]) #input can be ('chr', pos)

a=' bamsnap -ref /data/jaesoon/DB/gunhee/pig_all/Sus_scrofa.Sscrofa11.1.dna.toplevel.fa -bam p_6493_s_bl_g9_8.s.md.ir.bam p_6494_s_bl_g9_9.s.md.ir.bam p_6495_s_bl_g9_10.s.md.ir.bam p_6496_s_bl_g9_11.s.md.ir.bam p_6497_s_bl_g9_12.s.md.ir.bam p_6499_s_bl_g9_13.s.md.ir.bam p_6500_s_bl_g9_14.s.md.ir.bam p_6501_s_bl_g9_15.s.md.ir.bam p_6502_s_bl_g9_16.s.md.ir.bam p_6503_s_bl_g9_17.s.md.ir.bam p_6924_m_bl_g9_1.s.md.ir.bam p_6115_f_bl_g9_7.s.md.ir.bam -show_soft_clipped -pos hi -out /data/jaesoon/DB/SG/bamsnap/p6924_6115/p_2415.ZZ.hi.png'

list1=[]

for i in range(len(f)):
	list1.append(a.replace('hi',f[i]))

for j in range(len(list1)):
	print(list1[j])
	

