#!/home/jaesoon/miniconda3/bin/python

import numpy as np
import pandas as pd
import sys

input_df_1 = sys.argv[1]
input_df_2 = sys.argv[2]

df1 = pd.read_table(input_df_1, sep="\t", header = None, index_col= 0)
df2 = pd.read_table(input_df_2, sep="\t", header = None, index_col= None)

df1_t = df1.T
df2_t = df2.T

all_sum_1 = []
all_sum_2 = []

for i in df1:
  for j in df1_t:
    all_sum_1.append([i, j, str(df1[i][j])]) 
for i in df2:
  for j in df2_t:
    all_sum_2.append([i, j, str(df2[i][j])]) 

main_basket = []

for b in range(len(all_sum_1)):
  main_basket.append(all_sum_1[b][1])

sub_basket = []

for a in range(len(all_sum_2)):
  sub_basket.append(all_sum_2[a][2])


df1_trimmed = df1.drop(list(set(main_basket) - set(sub_basket)))

df1_trimmed.to_csv(f"{sys.argv[1]}.sub.txt", header=None, sep="\t") 