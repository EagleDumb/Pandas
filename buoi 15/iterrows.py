import pandas as pd

data = {'Name': ['John', 'Jane', 'Bob', 'Alice'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'London', 'Paris', 'Tokyo']}
df = pd.DataFrame(data)

for index, row in df.iterrows():
    print("----------------------------")
    print("index: ", index)
    print(f"Names: {row["Name"]}, Age: {row["Age"]}, City: {row["City"]}")

print("----------------------------------")
print(df)