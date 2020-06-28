import multiprocessing as mp
def job(x):
    return x*x

def multicore():
    # pool=mp.Pool() # 默認值為全部的CPU核
    pool=mp.Pool(processes=2) # 可自訂调用CPU核數量
    res=pool.map(job,range(10))
    print("by map():",res)
    res2=pool.apply_async(job,(100,)) # apply_async()中只能传递一个值，即apply_async()只能输入一组参数，并返回一个结果。
    print(res2.get()) # 用get获得结果
    # 用apply_async()输出多个迭代呢
    multi_res3=[pool.apply_async(job,(i,)) for i in range(10)]
    print("by apply_async():",[res3.get() for res3 in multi_res3]) # 同样在取出值时需要一个一个取出来

if __name__=="__main__":
    multicore()
