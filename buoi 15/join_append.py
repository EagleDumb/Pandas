import pandas as pd 

df1 = pd.DataFrame({'Name': ['John', 'Jane', 'Bob'],
                    'Age': [25, 30, 35],
                    'City': ['New York', 'London', 'Paris']})

df2 = pd.DataFrame({
                    'Salary': [50000, 60000, 55000],
                    'Department': ['IT', 'HR', 'Finance']
                    })

df_joined = pd.concat([df1, df2], axis = 1, join = "inner")

print(df_joined)