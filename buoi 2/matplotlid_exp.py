import matplotlib.pyplot as plt 
import numpy as np

xpoints = np.array([2018,2019,2020,2021,2022])
ypoints = np.array([10,8,7,9,12])

plt.title("biểu đồ sản lượng khoai mì theo năm", color = "black", backgroundcolor = "yellow")
plt.plot(xpoints,ypoints)
plt.show()