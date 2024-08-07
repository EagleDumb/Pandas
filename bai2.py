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

columns_list = df.columns
values_list = sum_data.values()

df.insert(len(columns_list), "DTB", values_list)


result_list = []
for i in values_list:
    if i >= 5:
        result_list.append("Pass")
    else:
        result_list.append("Fail")

print(result_list)
df.insert(len(columns_list)+1, "Note", result_list)

#bai 3 ko hieu lam

xeploai_list = []
for i in values_list:
    if i >= 9:
        xeploai_list.append("Excellent")
    elif i >= 7:
        xeploai_list.append("Good")
    elif i >= 5:
        xeploai_list.append("Average")
    else:
        xeploai_list.append("Below Average")

df["Xep Loai"] = xeploai_list

tinhhocbong = []
for i in xeploai_list:
    if i == "Excellent":
        tinhhocbong.append(100000)
    elif i == "Good":
        tinhhocbong.append(50000)
    else:
        tinhhocbong.append(0)

df["Hoc Bong"] = tinhhocbong


def check_subject (index):
    subject_list = ["Toán","Lý","Hoá","Văn","Sử","Địa","Anh","Pháp","Trung","Sinh"]
    return subject_list[index - 1] #use index to return the subject of the column

object_value = []

for row in df.itertuples(index = False): 
    goal_value = ""
    for j in range (len(row)):
        print(row[j])
        #if (str(type(row[j])) != "<class 'str'>") and (row[j] < 5): #if row[j] is not string AND row[j] < 5
            #goal_value = check_subject(j) + "" + goal_value #used to add in the subject
    #object_value.append(goal_value)



#df["Thi Lai"] = object_value

print(df)
#dataframe = pd.DataFrame(sum_data, index = [0])
#print(dataframe)
#dataframe.to_csv("C:/Pandas/csvtest.csv")

