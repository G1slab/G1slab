#!/home/jaesoon/miniconda3/bin/python

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

input_file = sys.argv[1]

df = pd.read_table(input_file, sep = "\t", header = None)

x = []
y = []

for i in range(len(df[0])):
	x.append(str(df[0][i]))
	y.append(df[1][i])

plt.plot(x, y, linewidth = 0.5)
plt.autoscale(enable = True)
plt.savefig(f'{input_file}.png', dpi=500 )


