#!/home/jaesoon/miniconda3/bin/python

import pandas as pd
import numpy as np
import sys

df1_file = sys.argv[1]
df2_file = sys.argv[2]

df1 = pd.read_table(df1_file, sep="\t", header=0) #header -> zero
df2 = pd.read_table(df2_file, sep="\t", header=0)

df_new = pd.merge(df1, df2, left_on='chrpos', right_on='chrpos', how='inner')

print(df_new)

x = list(df_new['vaf_each'])
y = list(df_new['vaf_main'])

import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Calculate the point density
xy = np.vstack([x, y])
z = gaussian_kde(xy)(xy)

fig, ax = plt.subplots()
ax.scatter(x, y, c=z, s=50)
plt.savefig(f'{sys.argv[2]}.eachsample_scatter_forp15PON.png', dpi=300)

