import pandas as pd
import numpy as np

index_data = [1, 4, 6, 7, 5]
ser = pd.Series([3, 5, 11, 9, 4], index=index_data)
#sort by index

print(ser.sort_index(ascending = True))