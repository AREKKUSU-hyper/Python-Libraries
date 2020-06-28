import numpy as np
a=np.array([1,2,2,0]).reshape(2,2)
b=np.arange(4).reshape(2,2)
print(a)
print(b)
print("---------------------")
print(a+b)
print(a-b)
print("---------------------")
c=b**2
print(c)
c1=10*np.sin(a)
print(c1)
print("---------------------")
print(b<3)
print(b==3) #輸出布林值T/F
print("---------------------")
print(a*b) #逐個相乘
print("---------------------")
c_dot=np.dot(a,b) #矩陣乘法
c_dot2=a.dot(b) #a已是numpy的array
print(c_dot-c_dot2) 
print("---------------------")
d=np.random.random((2,3)) #0~1隨機數字組成矩陣
print(d)
print("------")
print("sum: ",np.sum(d)) #整個矩陣求和
print("max: ",np.max(d))
print("min: ",np.min(d))
print("------")
print("sum: ",np.sum(d,axis=1)) #每行求一次和
print("max: ",np.max(d,axis=0)) #每列一次max
print("min: ",np.min(d,axis=1)) #每行一次min

