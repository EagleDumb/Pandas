#Cho dữ liệu sau: [1, 7, nan, 13, 8, 9, nan, 14]
#Lable có giá trị là: ['apple', 'blueberry', 'cherry', 'orange’, ‘lemon’, ‘lime’, ‘plum’,’pear’ ] 
#Hãy thay thế những dữ liệu bị lỗi thành 0
#Vẽ biểu đồ cột với tên là: Fruit supply by kind and color 
#Lable của cột y có tên là: fruit supply 
#Mỗi cột phải có một màu sắc khác nhau
#In ra data có giá trị lớn nhất
#Tính tổng của data

import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

label = ['apple', 'blueberry', 'cherry', 'orange', 'lemon', 'lime', 'plum','pear']
ser = pd.Series([1, 7, np.nan, 13, 8, 9, np.nan, 14], index = label)
ser2 = ser.fillna(0)
print(ser2)

plt.bar(ser2.index, ser2.values)
plt.show()