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

def meanvafcheck(l1): 
  ls=[]
  for i in range(len(l1)):
    if l1[i] != 0:
      ls.append(float(l1[i]))  
  if sum(ls)/len(ls) > 0.3:
    return True
  else:
    return False

for k in range(len(list2)):
  if meanvafcheck(list2[k]) == False: 
    list3.append(k)           

df_t = df_t.drop(list3, axis=1)

df_original = df_t.T 

print(df_original)

df_original.to_csv(out_file, index=False, header=None, sep="\t")