import pandas as pd

df = pd.read_csv("C:/Pandas/buoi 15/data2.csv")

ser = pd.Series(df["ID"])
ser2 = ser.dropna()
print(ser2)
print(ser2.max())
print(ser2.min())