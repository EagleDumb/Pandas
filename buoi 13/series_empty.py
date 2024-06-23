import pandas as pd
import numpy as np

data2 = pd.Series([{"A" : [np.NaN]}])
print(data2.empty)