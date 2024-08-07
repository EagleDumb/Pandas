import pandas as pd
import matplotlib.pyplot as plt
# Đọc file csv
df =  pd.read_csv('data.csv')

df.dropna(thresh=2, axis="columns", inplace = True)
df.dropna(thresh=2, axis="rows", inplace = True)
print(df)

#steps 
#1: get value for each student
#2: calculate the average for each student

sum_data = {}

for row in df.itertuples(index = False):
    sum_value = 0
    name_value = ""
    

    #check the data for each rows
    for j in row:
        if str(type(j)) != "<class 'str'>":
            print(j, end=" ")
            sum_value = sum_value + j
        
        else:
            name_value = j
    
    print("total of values: ", sum_value/(len(row) - 1))
    print("name of student: ", name_value)
    sum_data.update({name_value : sum_value/(len(row) - 1)})
    
print(sum_data)

dataframe = pd.DataFrame(sum_data, index = [0])
print(dataframe)
dataframe.to_csv("C:/Pandas/csvtest.csv")
colors1 = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "turquoise", "gray", "brown", "lavender", "magenta", "teal"]


fig, ax = plt.subplots()

container = ax.bar(sum_data.keys(), sum_data.values(), color = colors1)
plt.xticks(rotation = 45)

yLabels = [0, 2, 4, 6, 8, 10]

ax.bar_label(container, fmt=lambda x: f'{x:.1f}')
plt.yticks(yLabels)
plt.title("Student AVG")

plt.show()

# - Học sinh thi tất cả các môn với số điểm >=5 ghi là "Đạt"												
# - Học sinh học lớp chuyên mà thi môn chuyên có điểm < 5 hoặc có trên 1 môn thi có điểm < 5 thì ghi là "Hỏng"												
# - Học sinh thi có một môn điểm < 5 ghi là "Thi Lại"												
#   Tô màu: Hỏng - màu đỏ; Thi lại - màu xanh da trời												