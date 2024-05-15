import matplotlib.pyplot as plt 
import numpy as np    

x = [1, 2, 3, 4] 
y = [95, 38, 54, 35] 
labels = ["a","b","c","d"]

plt.plot(x,y)
plt.yticks(y, labels, rotation = "vertical")
plt.show()