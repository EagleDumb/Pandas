import pandas as pd
import numpy as np

df = pd.DataFrame({
    'col1': ['B', 'A', 'B', np.nan, 'D', 'C'],
    'col2': [2, 1, 9, 8, 7, 4],
    'col3': [0, 1, 9, 4, 2, 3],
    'col4': ['a', 'B', 'c', 'D', 'e', 'F']
})

#templist = []
#for label, content in df.items():
#    templist.append(label)

x1 = list(df.columns)
#x = df.sort_values(by = x1, ascending = True, na_position="first")
x = df.sort_values(by = "col1", key = lambda col: col.str.lower())

print(x)