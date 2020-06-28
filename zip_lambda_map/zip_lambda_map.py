a=[1,2,3]
b=[4,5,6]

# print(zip(a,b))
print(list(zip(a,b))) #列表化可視化
for i,j,k in zip(a,a,b):
    print(i/2,j*2,k**2)

def fun1(x,y):
    return (x+y)
print(fun1(2,3))

fun2=lambda x,y: x+y
print(fun2(2,3)) #跟fun1同樣意思

map(fun1,[1,0.1],[4,0.1]) # map把函數和元素一起輸入
print(list(map(fun1,[1,0.1],[4,0.4])))

