import pandas as pd
import numpy as np

ser = pd.Series([3,3,8,8,3,3,9,9])
print(ser.mode()) #returns the value that appears the most in Series