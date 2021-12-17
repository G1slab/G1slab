#!/home/jaesoon/miniconda3/bin/python
import sys
import pandas as pd
import numpy as np


input_file = sys.argv[1]
sample_num = sys.argv[2]
vaf = sys.argv[3]

df = pd.read_table(input_file, sep="\t", header=None)

df_t = df.T

list1 =[]

for i in range(0, len(df)):       
  for j in range(1, len(df_t)):   
    list1.append(str(df_t[i][j])) 

list2 = [list1[m:m+int(sample_num)] for m in range(0, len(list1), int(sample_num))]

list3 = []


#################################################################

def all_vaf_threshold_cut(ls1, cut):
  TF_basket = []
  for i in range(len(ls1)):
    if float(ls1[i]) > cut:
      TF_basket.append(False)
    else:
      TF_basket.append(True)
  if False in TF_basket:
    return False
  else:
    return True

###############################################################

for k in range(len(list2)):
  if  all_vaf_threshold_cut(list2[k], float(vaf)) == False: 
    list3.append(k)         



df_t = df_t.drop(list3, axis=1) 

df_original = df_t.T

df_original.to_csv(f"{sys.argv[1]}.vaf1cut{sys.argv[3]}.txt", index=False, header=None, sep="\t")