import pandas as pd
x_lable = ["a", "b", "c", "d"]
s = pd.Series([5,1,2,3], name="Hoa", index=x_lable)

pop_items = s.pop("c")
print("new s: ",s)
print("pop items: ",pop_items)