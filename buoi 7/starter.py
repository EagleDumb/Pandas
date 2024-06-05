import matplotlib.pyplot as plt 
import numpy as np

xLable = ["apple", "blueberry", "cherry", "orange"]
yLable = [0, 20, 40, 60, 80, 100]
Fruit_supply = [40, 100, 30, 55]
x = [0.75,1.5,2.25,3]
color_label = ["red", "green", "blue", "yellow"]
barLabel = ["apple", "blueberry", "cherry", "orange"]

plt.title("Fruit supply by kind and color")
plt.xticks(x, xLable)
plt.yticks(yLable)
plt.ylabel("fruit supply")
plt.bar(x,Fruit_supply, color = color_label, width = 0.5, label = barLabel)
plt.legend(loc = "upper right")
plt.show()