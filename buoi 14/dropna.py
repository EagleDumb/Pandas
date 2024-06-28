import pandas as pd
import numpy as np

ser = pd.Series([1., 2., np.nan, 4, None])

newser = pd.Series()
newser = ser.dropna()
print(ser.dropna())
print(ser)
print(newser)

# Chú ý dropna() không làm thay đổi giá trị gốc
# Nhằm làm sạch dữ liệu nhằm thực hiện các phép tính