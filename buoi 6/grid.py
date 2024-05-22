import matplotlib.pyplot as plt 
import numpy as np
plt.xlim(2010, 2016.5)
plt.ylim(0, 210)

yLabels = [0, 50, 100, 150, 200]
xLabels = [2010, 2013, 2015, 2016]
xValue = [2010,2013,2015,2016]

plt.xticks(xLabels,xValue)
plt.yticks(yLabels)

aLine = [100, 147.8, 166.9, 177.2]
bLine = [100, 136.2, 146.7, 152.8]
cLine = [100, 123.3, 117, 119.3]

plt.xlabel("year")
plt.ylabel("%")

plt.plot(xValue, aLine, "o--r", mec = "blue", ms = 20, mfc = "green")
plt.plot(xValue,bLine,"s--b")
plt.plot(xValue,cLine,"^--g")
plt.grid(True, color = "Blue", axis = "x", linewidth = "3", linestyle = "--")
#marker|linestyle|color
#"o--r" = o "circle" and -- "dashed lines" and r "red color"

#mec = color of outline
#mfc = color of marker
#ms = size of marker

plt.title("example")

plt.show()
