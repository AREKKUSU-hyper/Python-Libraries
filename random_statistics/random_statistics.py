# 隨機模組
import random
# 隨機選取
data=random.choice([1,5,6,10,20])
print(data)
data=random.sample([1,5,6,10,20],3)
print(data)
# 隨機(就地)調換順序(洗牌)
data=[1,5,8,20]
random.shuffle(data)
print(data)
# 隨機取得亂數
data=random.random() # 0~1之間的隨機亂數
print(data)
# i.e.
data=random.uniform(60,100) # 60~100之間的隨機亂數
print(data)
# 取得常態分配亂數
data=random.normalvariate(100,10) # 平均數100,標準差10,得到資料多數90~110之間
print(data)

# 統計模組
import statistics as stat
data=stat.mean([1,4,5,8]) # 平均數
print(data)
data=stat.median([1,2,3,4,5,8,100]) # 中位數
print(data)
data=stat.stdev([1,2,3,4,5,8,100]) # 標準差
print(data)