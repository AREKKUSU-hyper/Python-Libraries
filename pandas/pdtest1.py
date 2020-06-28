import pandas as pd
import numpy as np
s=pd.Series([1,3,45,np.nan,8])
# print(s)
x=np.array([3]*4)
# print(x)

df0=pd.DataFrame(np.arange(12).reshape((3,4)))
# print(df0.iloc[1])

dates=pd.date_range("20191014",periods=6)
# print(dates)
df1=pd.DataFrame(np.random.randn(6,4),index=dates,columns=["A","B","C","D"])# index行 columns列 
# print(df1)

df2 = pd.DataFrame({
    'A' : 1.,
    'B' : pd.Timestamp('20130102'),
    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
    'D' : np.array([3] * 4,dtype='int32'),
    'E' : pd.Categorical(["test","train","test","train"]),
    'F' : 'foo'
})
print(df2)
print(df2.dtypes)
print(df2.index) #行的名字
print(df2.columns) #列的名字
print(df2.values) #值
print(df2.describe()) #只能運算數字，故會省略日期、字符串等

print(df2.T) #行列互換
print(df2.sort_index(axis=1,ascending=False)) #根據index排序，axis=1:列，非ascending=倒序
print(df2.sort_index(axis=0,ascending=False))
print(df2.sort_values(by="E")) #根據value排序