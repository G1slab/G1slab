#!/home/jaesoon/miniconda3/bin/python

import pandas as pd
import numpy as np
import sys

in_file = sys.argv[1]
out_file = sys.argv[2]

df = pd.read_table(in_file, sep="\t", header=None)

print(df)

df_t = df.T 

list1 =[]

for i in range(0, len(df)):
	  for j in range(1, len(df_t)):   
		  list1.append(str(df_t[i][j]))

list2 = [list1[m:m+10] for m in range(0, len(list1),10)] 

list3 = []

for k in range(len(list2)):
	  if list2[k].count('0.0') == 1 or list2[k].count('0.0') == 2 or list2[k].count('0.0') == 3 or list2[k].count('0.0') == 4 or list2[k].count('0.0') == 5 or list2[k].count('0.0') == 6 or list2[k].count('0.0') == 7 or list2[k].count('0.0') == 8 or list2[k].count('0.0') == 10 or list2[k].count('0.0') == 0: 
	      list3.append(k)           

print(list3)

df_t = df_t.drop(list3, axis=1) 

df_original = df_t.T 

print(df_original)

df_original.to_csv(out_file, index=False, header=None, sep="\t")
