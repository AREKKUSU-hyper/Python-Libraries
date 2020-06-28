import pandas as pd
import numpy as np

# merging two df by key/keys (may be used in database)
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
print(right)
res1=pd.merge(left,right,on="key")
print(res1)

# consider two keys
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
print(right)
res2=pd.merge(left,right,on=["key1","key2"])
print(res2)
# 合并时有4种方法how = ['left', 'right', 'outer', 'inner']，预设值how='inner'。
res2_2=pd.merge(left,right,on=["key1","key2"],how="right")
print(res2_2)

# indicator=True会将合并的记录放在新的一列
df1 = pd.DataFrame({'col1':[0,1], 'col_left':['a','b']})
df2 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
print(df1)
print(df2)
res3=pd.merge(df1,df2,on="col1",how="outer",indicator=True) # 依据col1进行合并，并启用indicator=True
print(res3)
res3_2 = pd.merge(df1, df2, on='col1', how='outer', indicator='indicator_column') # 自定indicator column的名称
print(res3_2)

# merged by index
left=pd.DataFrame({"A":["A0","A1","A2"],"B":["B0","B1","B2"]},index=["K0","K1","K2"])
right=pd.DataFrame({"C":["C0","C2","C3"],"D":["D0","D2","D3"]},index=["K0","K2","K3"])
print(left)
print(right)
res4=pd.merge(left,right,left_index=True,right_index=True,how="outer",indicator=True) # 依据左右资料集的index进行合并
print(res4)

# 使用suffixes解决overlapping的问题
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
print(boys)
print(girls)
res5=pd.merge(boys,girls,on="k",left_index=True,suffixes=["_boys","_girls"],how="inner")
print(res5)
