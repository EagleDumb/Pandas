import matplotlib.pyplot as plt 
import numpy as np

y = np.array([80,20,30,10])
y_label = np.array(["Apples", "Banana", "Melons", "Berries"])
colorlabels = np.array(["c", "green", "yellow", "purple"])
myexplode = np.array([0.2,0,0,0])

plt.pie(y, labels = y_label, startangle = 90, colors = colorlabels, explode = myexplode)
plt.legend()
plt.show()