#!/home/jaesoon/miniconda3/bin/python

import sys
import pandas as pd
import numpy as np

input_csv = sys.argv[1]

df = pd.read_table(input_csv, sep="\t", header=None)

df_t = df.T

row = []

for i in range(len(df)):
  row.append(list(df_t[i]))

def list_extract(s1):      
  return s1[:s1.rfind('_')]

def row_list_modifier(ls1): 
  for i in range(len(ls1)):
    if "(" in ls1[i]:
      ls1[i] = eval(ls1[i])
    else:
      ls1[i] = list_extract(ls1[i])
  return ls1

def one_to_one_compare(list1, list2): 
  TF_basket = []
  for i in range(1, len(list1)):
    if abs(eval(list1[i])[0] - eval(list2[i])[0]) <= 1 and  abs(eval(list1[i])[1] - eval(list2[i])[1]) == 0:
      TF_basket.append(True)
    elif abs(eval(list1[i])[0] - eval(list2[i])[0])  == 0 and  abs(eval(list1[i])[1] - eval(list2[i])[1]) <= 2:  
      TF_basket.append(True)
    else:
      TF_basket.append(False)
  if True in TF_basket:
    return 'Fake'
  else:
    return "Real"


def compare_lists(l1, l2, par): 
  for i in range(len(l1)):
    if abs(int(l1[0][1]) - int(l2[0][1])) < par and one_to_one_compare(l1, l2) == "Fake":
      return 'Del' +"_"+ str(abs(int(l1[0][1]) - int(l2[0][1])))
    else:
      return 'Save' +"_"+ str(abs(int(l1[0][1]) - int(l2[0][1])))



row_modified = [] 

for j in range(len(row)):
  row_modified.append(row_list_modifier(row[j]))

del_index = []

for k in range(len(row_modified) - 1):
  del_index.append(str(compare_lists(row_modified[k], row_modified[k+1], 100)))


del_index_plus = []

del_index_plus = del_index + ["Save_10000"]

final_index = []

for m in range(len(del_index_plus) - 1):
  if "Del" in del_index_plus[m]:
    final_index.append(m+1)

for n in final_index:
  del_index_plus[n] = "Del_ch"       

  
with open(f'{sys.argv[1]}.annot.txt', 'w') as writefile:
    for l in del_index_plus:
      print(l)
      writefile.write(l + '\n')