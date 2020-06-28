import pandas as pd
import numpy as np
dates=pd.date_range("20191017",periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=["A","B","C","D"])

df.iloc[2,2]=1111
df.loc["20191018","B"]=2222
df[df.A<=0]=0
df.D[df.A>12]=-1
df["F"]=np.nan # 加空的列
df["E"]=pd.Series([1,2,3,4,5,6],index=dates)
df.loc["20191018","F"]=666
print(df)

# 處裡缺失的數據
print(df.dropna(axis=1,how="all")) #how={"any","all"}
print(df.dropna(axis=1,how="any")) #丟棄不完整的數據 #axis=1對列處理
print(df.dropna(axis=0,how="any")) #axis=1對列處理
print("--------------------------")

# 補足缺失的數據
print(df.fillna(value=0))

# 檢查有無缺失的數據
print(df.isnull())
print(np.any(df.isnull())==True) # np.any() 確認是否包含一次
