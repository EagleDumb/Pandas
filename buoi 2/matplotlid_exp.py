import matplotlib.pyplot as plt 
import numpy as np

xpoints = np.array([0,2,4,6,8,10])
ypoints = np.array([0,2000,4000,6000,8000,10000])

plt.title("exp", color = "black", backgroundcolor = "yellow", fontsize = 18)
plt.plot(xpoints,ypoints, ls = "None")
plt.show()