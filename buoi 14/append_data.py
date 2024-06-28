import pandas as pd
import numpy as np

s1 = pd.Series(["a", "b"])
s2 = pd.Series(["c", "d"])
label = [0,1,2,3]
#it merges the values but doesnt go in order of 0 1 2 3 4
#value merged is ordered in which one is being entered in first 
s3 = pd.concat([s1, s2]).values
s3 = pd.Series(s3, index = [0,1,2,3])
print(s3)
