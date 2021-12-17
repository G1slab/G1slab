#!/home/jaesoon/miniconda3/bin/python

import sys

in_file = sys.argv[1]
cluster_num = sys.argv[2]

with open(in_file) as f:
	content = f.readlines()

content = [int(x.strip()) for x in content]

list2 = [content[m:m+cluster_num] for m in range(0, len(content), cluster_num)]

for i in range(len(list2)):
  print(sum(list2[i]))