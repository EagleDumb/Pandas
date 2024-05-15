import matplotlib.pyplot as plt 
import numpy as np

xpoints = np.array([1,10, 3, 4])
ypoints = np.array([3,1, 8, 10])

plt.title("title")
plt.plot(xpoints, color = "r", linewidth = "5")
plt.plot(ypoints, color = "blue", linewidth = "5")
plt.show()