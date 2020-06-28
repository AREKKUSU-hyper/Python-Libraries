import pandas as pd
import numpy as np
dates=pd.date_range("20191014",periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=["A","B","C","D"])
print(df["B"]==df.B)
print(df[0:3])
print(df["20191015":"20191017"])

# select by label: loc
print(df.loc["20191017"])
print(df.loc[:,["A","B"]])
print(df.loc["20191016":"20191017",["A","B"]])

# select by position: iloc
print(df.iloc[2:4,0:2])
print(df.iloc[[1,3,5],0:2]) # 逐個不連續篩選

# mixed selection: ix
print(df.ix[:3,["A","C"]])

# Boolean indexing
print(df)
print(df[df.A<=8])