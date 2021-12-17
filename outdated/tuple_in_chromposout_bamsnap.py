#!/home/jaesoon/miniconda3/bin/python
#change () tuple to 1:123124 bamsnapformat

import sys

in_file = sys.argv[1]

with open(in_file) as f:
	content = f.readlines()

content = [x.strip() for x in content]

for i in range(len(content)):
	content[i] = eval(content[i])

for j in range(len(content)):
	print(content[j][0] + ":" + str(content[j][1]))
