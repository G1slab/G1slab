#!/home/jaesoon/miniconda3/bin/python

import pandas as pd
import numpy as np
import sys

M_list=sys.argv[1]

with open(M_list) as f:
	f=f.read().splitlines()

for k in range(len(f)):
	f[k] = str(eval(f[k])[0]) + ":" +str(eval(f[k])[1]) #input can be ('chr', pos)

a='bamsnap -ref /data/jaesoon/DB/Mouse_Raw/GRCm38.fa -bam sample_m_296_271_s_tl_0110_1.s.md.ir.bam sample_m_296_271_s_tl_0110_2.s.md.ir.bam sample_m_296_271_s_tl_0110_3.s.md.ir.bam sample_m_296_271_s_tl_0110_4.s.md.ir.bam sample_m_296_271_s_tl_0110_5.s.md.ir.bam sample_m_296_271_s_tl_0501_1.s.md.ir.bam sample_m_296_271_s_tl_0501_2.s.md.ir.bam sample_m_296_271_s_tl_0501_3.s.md.ir.bam sample_m_296_271_s_tl_0501_4.s.md.ir.bam sample_m_296_271_s_tl_0501_5.s.md.ir.bam sample_m_271_female_f_tl.s.md.ir.bam sample_M_296_Male_M_TL.s.md.ir.bam -show_soft_clipped -pos hi -out /data/jaesoon/DB/SG/bamsnap/296_271.merged.hi.png'

list1=[]

for i in range(len(f)):
	list1.append(a.replace('hi',f[i]))

for j in range(len(list1)):
	print(list1[j])
	

