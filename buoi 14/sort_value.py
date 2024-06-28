import pandas as pd
import numpy as np

ser = pd.Series([3,5,11,9,4])
#ascending is used to determine if its from smallest to biggest or biggest to smallest
print(ser.sort_values(ascending = False))