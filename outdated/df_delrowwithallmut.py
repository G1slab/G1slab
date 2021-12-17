#!/home/jaesoon/miniconda2/bin/python

import sys
import pandas as pd
import numpy

file = sys.argv[1]

df=pd.read_csv(file,delimiter='\t') #tsv file call
#print(df)

df = df[~(df == 0).any(axis=1)] #  ~ : XOR , any(axis=1) : returns True if any of the columns are True
#df = df[~(df == 1).any(axis=1)] # axis: 0 or 'index' , 1 or 'columns', None
pd.set_option('display.max_seq_items', None) # Not omitted

df.to_csv(f'{sys.argv[1]}.delrowwithallmut.txt',sep='\t',index=False) #without index
