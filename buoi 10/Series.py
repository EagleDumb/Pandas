import pandas as pd

x_label = ["a", "b", "c", "d"]
s = pd.Series([5,1,2,3], name = "title", index = x_label)
print(s)