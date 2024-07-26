import matplotlib.pyplot as plt 

plt.figure()

line1, = plt.plot([1, 2, 3, 4], [1, 4, 9, 16], label='Đường thẳng 1')
line2, = plt.plot([1, 2, 3, 4], [2, 5, 10, 17], label='Đường thẳng 2')
line3, = plt.plot([1, 2, 3, 4], [3, 6, 11, 18], label='Đường thẳng 3')

plt.legend([line1,line2,line3], ["Label1", "Label2", "Label3"])
plt.show()