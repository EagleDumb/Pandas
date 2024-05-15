import matplotlib.pyplot as plt 
import numpy as np

x = [1,4,3,2,8]
y = [6,8,7,2,3]

plt.ylim(0,10) #y limit
plt.xlim(0,10) #x limit
plt.plot(x, y, label = 'EXP')
plt.title('exmp')
plt.show()