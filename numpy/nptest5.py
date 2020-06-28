import numpy as np
A=np.arange(3,15).reshape(3,4)
print(A)
print(A[2])
print(A[1][1]==A[1,1])
print(A[:,1]) # 第一列的所有數
print(A[1,1:3])

print("-------------")
x=0
for row in A:
    print("第%s行" % x,row)
    x+=1
y=0

for column in A.T:
    print("第%s列" % y,column)
    y+=1
print("-------------")
print(A.flatten())
for item in A.flat: # 先將矩陣轉變為一行的序列，以便抓出其中每一項
    print(item)