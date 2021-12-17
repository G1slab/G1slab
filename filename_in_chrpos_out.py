#!/home/jaesoon/miniconda3/bin/python

import pandas as pd
import numpy as np
import sys

M_list=sys.argv[1]

with open(M_list) as list1:
	list1=list1.read().splitlines()

for i in range(len(list1)):  
  list1[i] = list1[i][(list1[i].find('d.') + 2):list1[i].rfind('.')]  #set universial index for all filenames
  list1[i] = (list1[i][:list1[i].find(':')],int(list1[i][list1[i].find(':')+1:]))  #chr pos to tuple

for j in list1:
	print(j)