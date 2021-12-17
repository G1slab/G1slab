#!/home/jaesoon/miniconda3/bin/python

import sys
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')


input_file = sys.argv[1]

df = pd.read_table(input_file, sep = "\t", header = None)

y = [int(a) for a in df[3]]

n = 1000 
y_1000 = [y[i * n:(i + 1) * n] for i in range((len(y) + n - 1) // n )] 

y_1000_mean = [sum(a)/len(a) for a in y_1000]

x = [b for b in range(len(y_1000_mean))]

plt.plot(x, y_1000_mean, linewidth = 0.5)
plt.autoscale(enable = True)
plt.savefig(f'{input_file}.png', dpi=500 )


