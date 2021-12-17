#!/home/jaesoon/miniconda3/bin/python

import pandas as pd
import numpy as np
import sys

input_file = sys.argv[1]

df = pd.read_table(input_file, sep="\t", header=None)

df_t = df.T

list1 =[]

for i in range(0, len(df)):       
  for j in range(1, len(df_t)):   
    list1.append(eval(df_t[i][j])) 

list2 = [list1[m:m+10] for m in range(0, len(list1),10)]

#print(list2)

def list_in_list_wholevaf(ls):
  depth = 0
  alt = 0
  for i in range(len(ls)):
    depth += ls[i][1]
    alt += ls[i][0]
  return alt/depth

list3 = []

for k in range(len(list2)):
  list3.append(list_in_list_wholevaf(list2[k]))

#print(list3)

list4 = []

for l in range(len(list3)):
  #if list3[l] > 0:
    list4.append(list3[l])

for n in list4:
	print(n)