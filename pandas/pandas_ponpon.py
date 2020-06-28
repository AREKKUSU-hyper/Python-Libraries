import pandas as pd
import numpy as np
data=pd.Series([-3,-20,5,45,np.nan],index=["a","b","c","d","e"])

# 資料索引: 根據順序或索引取得資料
print(data)
print(data[0],data["a"],data.a)

# 觀察資料
print("資料型態",data.dtype)
print("資料數量",data.size)
print("資料索引",data.index)

# 數學、統計運算
print("和",data.sum())
print("最大值",data.max())
print("最小值",data.min())
print("積",data.prod())
print("平均值",data.mean())
print("中位數",data.median())
print("標準差",data.std())
print("前幾大"+"\n",data.nlargest(3))
print("前幾小"+"\n",data.nsmallest(2))

# 字串操作
data=pd.Series(["您好","Python","Pandas"])
print("所有字串變小寫"+"\n",data.str.lower())
print("所有字串變大寫"+"\n",data.str.upper())
print("算出字串長度"+"\n",data.str.len())
print("將字串串一起",data.str.cat(sep="/")) # 用sep自訂串接的符號
print("判斷字串中是否包含()"+"\n",data.str.contains("P"))
print("取代"+"\n",data.str.replace("P","屁"))


