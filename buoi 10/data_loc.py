import pandas as pd
import numpy as np

df = pd.read_csv("C:/Pandas/buoi 10/test.csv")
ser = pd.Series(df["Name"]) #value for Name column
print(ser)

data = ser.head(3) #return value from 0 to 2
print(data)

print(data.loc[0:1]) #return value from 0 to 1