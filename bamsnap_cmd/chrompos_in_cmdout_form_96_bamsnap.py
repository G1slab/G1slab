#!/home/jaesoon/miniconda3/bin/python

import pandas as pd
import numpy as np
import sys

M_list=sys.argv[1]

with open(M_list) as f:
	f=f.read().splitlines()

for k in range(len(f)):
	f[k] = str(eval(f[k])[0]) + ":" +str(eval(f[k])[1]) #input can be ('chr', pos)

a='bamsnap -ref /data/jaesoon/DB/gunhee/mouse_all/GRCm38.fa -bam mouse_96_un1.71_PA7_G4.s.md.ir.bam mouse_96_un2.96L_CHM3_F12.s.md.ir.bam mouse_96_un3.96L_D4M2_A5.s.md.ir.bam mouse_96_un4.96L_KI8_D1.s.md.ir.bam mouse_96_un5.96L_ST6_c8.s.md.ir.bam mouse_96_un6.96_AO6_2b3.s.md.ir.bam -show_soft_clipped -pos hi -out /data/jaesoon/DB/SG/bamsnap/mouse_96.merged.hi.png'

list1=[]

for i in range(len(f)):
	list1.append(a.replace('hi',f[i]))

for j in range(len(list1)):
	print(list1[j])