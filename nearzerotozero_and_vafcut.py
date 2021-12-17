#!/home/jaesoon/miniconda3/bin/python

import sys
import pandas as pd
import numpy as np

input_file = sys.argv[1]
threshold = sys.argv[2]
sample_num = sys.argv[3]
mean_vaf_threshold = sys.argv[4]

df = pd.read_table(input_file, sep="\t", header=None)

df_t = df.T

list1 =[]

for i in range(0, len(df)):       
  for j in range(1, len(df_t)):   
    if float(df_t[i][j]) < float(threshold):   
      df_t[i][j] = "0"
    list1.append(str(df_t[i][j]))

list2 = [list1[m:m+int(sample_num)] for m in range(0, len(list1), int(sample_num))]

list3 = []


################################################################# 

def mean_vaf_cut(ls1, cut):
  nozero_basket = []
  for i in range(len(ls1)):
    if str(ls1[i]) != "0":
      nozero_basket.append(float(ls1[i]))
  if len(nozero_basket) == 0:
    return False
  elif sum(nozero_basket)/len(nozero_basket) > cut:
    return True
  else:
    return False


###############################################################

for k in range(len(list2)):
  if  mean_vaf_cut(list2[k], float(mean_vaf_threshold)) == False: 
    list3.append(k)         

df_t = df_t.drop(list3, axis=1) 

df_original = df_t.T

df_original.to_csv(f"{sys.argv[1]}.selfvafandmeanvaf{sys.argv[3]}.txt", index=False, header=None, sep="\t")
