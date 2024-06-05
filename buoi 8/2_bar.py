import matplotlib.pyplot as plt 
import numpy as np

# Dữ liệu đầu vào 
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
y1 = np.array([4, 5, 1, 11])

x_len = np.arange(len(x))  # Trả về một mảng có giá trị từ 0 đến n - 1
print("x_len: ", x_len)
a_colors = np.array(["red", "blue", "green", "#4CAF50"]) # list chứa màu sắc

fig, ax = plt.subplots(layout = "constrained")

width = 0.25
multiplier = 2
offset = width * multiplier

ax.bar(x_len + offset, y, color = a_colors, align = "center", width = 0.2)
ax.bar(x_len, y1, color = a_colors, align = "center", width = 0.2)

ax.set_xticklabels(x)
ax.set_xticks(x_len)

plt.show()