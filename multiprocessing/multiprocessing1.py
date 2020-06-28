import multiprocessing as mp
# import threading as td

def job(q):
    # print("AAAAA")
    result=0
    for i in range(3):
        result+=i+i**2+i**3
    q.put(result) # queue

if __name__=="__main__":
    q=mp.Queue()
    # t1=td.Thread(target=job,args=(1,2))
    p1=mp.Process(target=job,args=(q,)) # args 若只有一個值要加「,」表示可疊代
    p2=mp.Process(target=job,args=(q,)) 
    # t1.start()
    p1.start()
    p2.start()
    # t1.join()
    p2.join()
    p1.join()
    res1=q.get()
    res2=q.get()
    print(res1+res2)