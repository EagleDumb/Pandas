import matplotlib.pyplot as plt 
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3,8,1,10])

a_colors = np.array(["red", "blue", "green", "#4CAF50"])

plt.bar(x,y,color = a_colors)
plt.plot(x,y)
plt.show()