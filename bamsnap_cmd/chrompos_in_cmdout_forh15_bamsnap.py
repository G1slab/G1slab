#!/home/jaesoon/miniconda3/bin/python

import pandas as pd
import numpy as np
import sys

M_list=sys.argv[1]

with open(M_list) as f:
	f=f.read().splitlines()

for k in range(len(f)):
	f[k] = str(eval(f[k])[0]) + ":" +str(eval(f[k])[1]) #input can be ('chr', pos)

a= 'bamsnap -ref /data/sg/ref/human_g1k_v37.fasta -bam 15C9Fb_6001E2.s.md.ir.bam 15L21Fb_1001D4.s.md.ir.bam 15L36Fb_001A6.s.md.ir.bam 15L49Fb_2001E2.s.md.ir.bam 15L55MS_1001A7.s.md.ir.bam 15LNMS_2001H5.s.md.ir.bam 15LSRMS_5001H4.s.md.ir.bam 15R126Fb_1001B4.s.md.ir.bam 15R36Fb_5001F1.s.md.ir.bam 15R76Fb_6001A8.s.md.ir.bam -save_image_only -silence -show_soft_clipped -pos hi -out /data/jaesoon/DB/SG/bamsnap/p_15.merged.hi.png'
list1=[]

for i in range(len(f)):
	list1.append(a.replace('hi',f[i]))

for j in range(len(list1)):
	print(list1[j])
	

