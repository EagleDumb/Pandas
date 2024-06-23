import pandas as pd
import numpy as np

df = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]), columns = ['A', "B", "C"], index = ["10", "20", "30"])
print(df)