import multiprocessing as mp
import time
# value1 = mp.Value("i",1)
# value2 = mp.Value('d', 3.14)
# array = mp.Array("i",[1,2,3]) # array只能是一维的

def job(v,num,lock):
    # 保证运行时一个进程的对锁内内容的独占
    lock.acquire() # 锁住
    for _ in range(10):
        time.sleep(0.3)
        v.value+=num # v.value获取共享变量值
        print(v.value)
    lock.release() # 释放

def multicore():
    v=mp.Value("i",0) # 定义共享变量
    lock=mp.Lock()
    p1=mp.Process(target=job,args=(v,1,lock),name="P1")
    p2=mp.Process(target=job,args=(v,3,lock),name="P2")
    p1.start()
    p2.start()
    p2.join()
    p1.join()

if __name__=="__main__":
    multicore()