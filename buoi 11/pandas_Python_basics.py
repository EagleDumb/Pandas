import pandas as pd
import numpy as np

d = {"colls1" : [1, 2], "colls2" : [3,4]}
df = pd.DataFrame(np.array([[1,2],[3,4]]), columns = ["AB", "DC"], index = [10, 20])

dfType = df.dtypes
print(df)
print("type: ", dfType)