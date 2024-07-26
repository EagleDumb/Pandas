list_a = []


for i in range (3):
    temp_list = []
    for j in range (3):
        temp_list.append(int(input("Number: ")))
    list_a.append(temp_list)
largestnumber = list_a[0][0]
smallestnumber = list_a[0][0]

print(list_a)

for i in list_a:
    for j in i:
        print(j)
        if largestnumber < j:
            largestnumber = j
        
        if smallestnumber > j:
            smallestnumber = j


print(str(largestnumber))
print(str(smallestnumber))

    