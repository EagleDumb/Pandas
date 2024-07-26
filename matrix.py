a_matrix = [[1, 8, 7], 
            [2, 7, 9], 
            [4, 3, 5]
            ]

maxnumber = a_matrix[0][0]

for i in a_matrix:
    for j in i:
        if j > maxnumber:
            maxnumber = j

print(maxnumber)