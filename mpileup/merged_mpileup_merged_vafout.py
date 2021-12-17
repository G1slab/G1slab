#!/home/jaesoon/miniconda3/bin/python

import pandas as pd
import numpy as np
import sys

in_file = sys.argv[1]

df = pd.read_table(in_file, sep="\t", header=None)

df_t = df.T

def indel_count(str1): #count indels -2AATA like this
  indel_list = []

  for i in range(len(str1)):
   if str1[i] == '+' or str1[i] == '-':
     indel_list.append(str1[i:i + int(str1[i+1]) + 2])

  indel_list_set = list(set(indel_list))

  for j in range(len(indel_list_set)):
   indel_list_set[j] = indel_list_set[j]+ ':' +str(indel_list.count(indel_list_set[j]))

  return indel_list_set #return value : ['-3AAA:2', '+4TTAT:2', '+2AC:1']




def indel_count_dup(str1): #count indels but express dups
  indel_list = []

  for i in range(len(str1)):
   if str1[i] == '+' or str1[i] == '-':
     indel_list.append(str1[i:i + int(str1[i+1]) + 2])

  return indel_list #return value : ['+2AC', '+2AC', '-3AAA', '-3AAA', '+4TTAT', '+4TTAT']



def ls_alphabet_cal(ls, al): #count A, T, G, C numbers
  ls_str = ''.join(ls)
  return ls_str.count(al)

def list_offspring(x):            #for splitting by F
  a=x
  b=a.split('F')
  c=[]
  for i in range(len(b)):
    if b[i]!='' and b[i]!=':':
      c.append(b[i])
  return c


def indel_detail(x):              # show detailed distribution of indels through offsprings
  a = list_offspring(x)
  list1=[]
  for j in a:
      for i in range(len(j)):
        if j[i] == '+' or j[i] == '-':
          h=j[i+1]
          h=int(h)
          c=j[i:i+2+h]
          if c not in list1:
            list1.append(c)
  list2=[]
  for q in list1:
    count=0
    for k in a:
      if q in k:
        count+=1
    list2.append([q,str(count)+"offspring"])
  return list2

def snvs_detail(x):        # show detailed distribution of snvs through offsprings -> similar to indel_detail
  a = list_offspring(x)
  S=['A','T','G','C']
  list1=[]
  for j in a:
    for i in range(len(S)):
      if S[i] not in list1 and S[i] in j:
        list1.append(S[i])
  list2=[]
  for q in list1:
    count=0
    for k in a:
      if q in k:
        count+=1
    list2.append([q,str(count)+"offspring"])

  return list2

def remove_indel(st):        #for input for snvs_indel, remove indels and remain only snvs
  remove_list = [x[0] for x in indel_detail(st)]
  for i in remove_list:
    st = st.replace(i, '')
  return st


def merged_vafcal(ls):
  ls_cut = ls[3:]       #not including chr/pos
  c_spchr = 0             #count . , 
  c_a = 0
  c_t = 0
  c_g = 0
  c_c = 0
  ls_str = []
  for i in range(len(ls_cut)):
    if type(ls_cut[i]) == str:
      ls_str.append(ls_cut[i]) #only append '...,.,.,...,a.,.,' like this not 33, 35, 34~~~
  ls_to_str = ''.join(ls_str)  #make long string with appended only strings
  ls_to_str = ls_to_str.upper() #make all string uppercase to merge all indels
  indel_A = ls_alphabet_cal(indel_count_dup(ls_to_str), "A")
  indel_T = ls_alphabet_cal(indel_count_dup(ls_to_str), "T")
  indel_G = ls_alphabet_cal(indel_count_dup(ls_to_str), "G")
  indel_C = ls_alphabet_cal(indel_count_dup(ls_to_str), "C")
  c_spchr += ls_to_str.count('.')
  c_spchr += ls_to_str.count(',')
  c_spchr += ls_to_str.count('*') 
 #c_spchr += ls_to_str.count('^') 
 #c_spchr -= 10                             #### just count . and , -> the number will be perfectly matched for no variants
  c_a += ls_to_str.count('a')
  c_a += ls_to_str.count('A')
  c_t += ls_to_str.count('t')
  c_t += ls_to_str.count('T')
  c_g += ls_to_str.count('g')
  c_g += ls_to_str.count('G')
  c_c += ls_to_str.count('c')
  c_c += ls_to_str.count('C')
  c_a -= indel_A                          #delete number of ATGCs present in indels -> if don't delete, vaf calculation is above original
  c_t -= indel_T
  c_g -= indel_G
  c_c -= indel_C
  if sum(filter(lambda i: isinstance(i, int), ls_cut)) == 0: # for division by zero error
  	return 'None'
  else:
  	return  str((str(ls[0]), ls[1])) + "\t" + str(1 - c_spchr/sum(filter(lambda i: isinstance(i, int), ls_cut)))\
		+ "\t" + "a" + str(c_a/sum(filter(lambda i: isinstance(i, int), ls_cut))) + "\t" + "t" + str(c_t/sum(filter(lambda i: isinstance(i, int), ls_cut)))\
		+ "\t" + "g" + str(c_g/sum(filter(lambda i: isinstance(i, int), ls_cut))) + "\t" + "c" + str(c_c/sum(filter(lambda i: isinstance(i, int), ls_cut)))\
		+  "\t" + str(indel_count(ls_to_str)) +  "\t" + str(indel_detail(ls_to_str)) + "\t" +  str(snvs_detail(remove_indel(ls_to_str)))
  #sum(filter~~~) -> sum of all ints present in a list ##better to count  . , and minus from one -> a t g c and indel hard to count

for j in range(len(df)):
  print(merged_vafcal(list(df_t[j])))
