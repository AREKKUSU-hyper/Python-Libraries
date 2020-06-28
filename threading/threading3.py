import threading
import time
from queue import Queue

# 对列表的每个元素进行平方计算，将结果保存在队列中
def job(l,q):
    for i in range(len(l)):
        l[i]=l[i]**2
        time.sleep(1)
    q.put(l)

def multithreading():
    q=Queue() # q中存放返回值，代替return的返回值
    threads=[]
    data=[[1,2,3],[3,4,5],[4,4,4],[5,5,5]]
    for i in range(4):
        T=threading.Thread(target=job,args=(data[i],q))
        T.start()
        threads.append(T)
    for thread in threads:
        thread.join()
    results=[]
    for x in range(4):
        results.append(q.get()) # q.get()按顺序从q中拿出一个值
    print(results)
    
if __name__=="__main__":
    multithreading()

