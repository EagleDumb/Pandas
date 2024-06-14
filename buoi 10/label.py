import pandas as pd
import numpy as np

data = np.array(['1' ,'e' ,'b' ,'k' ,'s' ,'f' , 'o','t' ,'g' ,'m','e','k','s'])
ser = pd.Series(data, index = ["10","11","12","13","n","15","16","17","l",19 ,20 ,21 ,22])

print(ser[0:6])
