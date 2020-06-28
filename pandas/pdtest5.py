import pandas as pd
import numpy as np
# concatenating
df1=pd.DataFrame(np.ones((3,4))*0,columns=["a","b","c","d"])
df2=pd.DataFrame(np.ones((3,4))*1,columns=["a","b","c","d"])
df3=pd.DataFrame(np.ones((3,4))*2,columns=["a","b","c","d"])
res1=pd.concat([df1,df2,df3],axis=0,ignore_index=True) # axis=0豎向; axis=1橫向。ignore_index=True:index重排。
print(res1)

# join, ["inner","outer"]
df4=pd.DataFrame(np.ones((3,4))*0,columns=["a","b","c","d"],index=[1,2,3])
df5=pd.DataFrame(np.ones((3,4))*1,columns=["b","c","d","e"],index=[2,3,4])
res2=pd.concat([df4,df5],axis=0,join="outer",sort=True) # concat默認就是join="outer"
print(res2)
res3=pd.concat([df4,df5],axis=0,join="inner",ignore_index=True)
print(res3)

# join_axes
res4=pd.concat([df4,df5],axis=1,join_axes=[df4.index]) # 按照df1的index進行合併
print(res4)

# append
# res5=df1.append(df2,ignore_index=True)
# print(res5)
res5=df1.append([df2,df3],ignore_index=True)
print((res1==res5).all())
s1=pd.Series([1,2,3,4],index=["a","b","c","d"])
res6=df1.append(s1,ignore_index=True)
print(res6)

# 用==判断只能返回一个判断矩阵，表示其中每一个元素是否对应相等。
# print((a==b).all()) 如果两个矩阵中的所有元素对应相等，则返回True，反之返回False。
# 判断两个矩阵中是否有相等的元素，有任何一个相等就行，这种情况就可以用.any()