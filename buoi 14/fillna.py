import pandas as pd
import numpy as np

ser = pd.Series([1., 2., np.nan, 4, None])

newser = pd.Series()
newser = ser.fillna(0)
print(ser.fillna(0))
print(ser)
print(newser)