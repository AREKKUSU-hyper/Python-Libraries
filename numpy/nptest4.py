import numpy as np
A=np.arange(2,14).reshape((3,4))
print(np.argmin(A)) # 索引最小值
print(np.argmax(A))

print(np.mean(A)) # 求平均值
print(A.mean()) # 亦可
print(np.average(A))

print(np.median(A)) # 求中位數
print("-------")

print(A)
print(np.cumsum(A)) # 逐步累加
print(np.diff(A)) # 每兩數之間的差

print(np.nonzero(A))
print("-------")
B=np.arange(14,2,-1).reshape((3,4))
print(B)
print(np.sort(B)) # 逐行   排序
print("-------")
print(np.transpose(A)) # 矩陣反向(行列互換)
print(A.T) # 矩陣反向(行列互換)
print((A.T).dot(A))
print("----------------------")
print(A)
print(np.clip(A,5,9)) # array A中5~9之間數保留，小於5變5,大於9變9
print(np.mean(A,axis=0)) # axis=0 對列計算
print(np.mean(A,axis=1)) # axis=1 對行計算
