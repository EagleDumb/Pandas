import matplotlib.pyplot as plt 
import numpy as np    

x = [- 1, 4, 3, 2, 8]  # list x , giá trị nhỏ nhất và giá trị lớn nhất của mảng là bao nhiêu
y = [6, 8, 7, -2, 3]  # list y

plt.xlim(-1,10)
plt.ylim(-2,10)
plt.plot(x,y, label = "EXP", color = "r")
plt.title("exp")

plt.show()