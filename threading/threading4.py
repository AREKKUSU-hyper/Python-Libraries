import threading
from queue import Queue
import time
import copy

def job(l,q):
    res=sum(l)
    q.put(res)

def multitreading(l):
    q=Queue()
    threads=[]
    for i in range(4):
        t=threading.Thread(target=job,args=(copy.copy(l),q),name="T%i" %i)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    total_th=0
    for result in range(4):
        total_th+=q.get()
    print(total_th)

def normal(l):
    total_n=sum(l)
    # total_n_4x=total_n*4
    # print(total_n_4x)
    print(total_n)

if __name__=="__main__":
    l=list(range(100000))
    s_t=time.time()
    normal(l*4)
    time_n=time.time()-s_t
    print("normal:",time_n)

    s_t=time.time()
    multitreading(l)
    time_th=time.time()-s_t
    print("multithreading:",time_th)
    diff=time_th-time_n
    print("使用多線程(4)為您省下%f秒" % diff)

