import pandas as pd
import numpy as np

data = {"courses" : "pandas", "Fees" : 20000, "Duration" : "30 days"}
s2 = pd.Series(data)
s2["ID"] = "0351"
print(s2)