import pandas as pd

# import os
# os.path.abspath("C:\Users\ALEX\Desktop\student.csv")

data=pd.read_csv(r"C:\Users\ALEX\Desktop\student.csv")
# 在字符串前加個r 是為了告訴編譯器這個string是個raw string，不要轉譯
# print(data)
NEW_data=data[data.gender=="Female"]
NEW_data.to_pickle("girls.pickle")
girls=pd.read_pickle("girls.pickle")
print(girls)