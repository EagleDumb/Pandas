import pandas as pd 

df1 = pd.DataFrame([['a', 1], 
                    ['b', 2]],
                   columns=['letter', 'number'])

df2 = pd.DataFrame([['c', 3], 
                    ['d', 4]],
                   columns=['letter', 'number'])

df3 = pd.concat([df1,df2], axis = 0, ignore_index=True)
print(df3)