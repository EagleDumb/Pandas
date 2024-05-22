import matplotlib.pyplot as plt 
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
a_colors = np.array(["red", "blue", "green", "#4CAF50"])
barlabel = np.array(["A", "B", "C", "D"])

plt.bar(x, y, color = a_colors, label = barlabel)
plt.legend(loc = "upper left")
plt.show()