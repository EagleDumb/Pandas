import pandas as pd
import numpy as np

data = np.array(['g','e','e','k','s','f', 'o','r','g','e','e','k','s'])
s = pd.Series(data, index =[11,12,13,14,15,16,17,18,19,20,21,22,23])

print(s[20])

#if index contains integer then use integer
#if index is string then have to use string to get the value