import matplotlib.pyplot as plt 
import numpy as np
plt.xlim(1, 5)
plt.ylim(0, 40)

x = [1, 2, 3, 4, 5]
y = [0, 10, 20, 30, 40]
#yLabel = ["0", "10", "20", "30", "40"]
xLabel = ["Month 1", "Month 2", "Month 3", "Month 4", "Month 5"]
Legendlist = ["Month 1", "Month 2", "Month 3", "Month 4", "Month 5"]

p = [19, 26, 23, 35, 36]
s = [16, 14, 19.5, 19.5, 12]
m = [5, 23, 21, 16, 29]

plt.title('LINE CHART INFOGRAPHIC')
plt.xticks(x,xLabel)
plt.yticks(y)

plt.plot(x,p, "o-r")
plt.plot(x,s,"^-b")
plt.plot(x,m,"s-y")
plt.legend(Legendlist, loc = "lower right")

plt.show()