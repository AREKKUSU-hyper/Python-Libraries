import time

data=[[1,2,3],[3,4,5],[4,4,4],[5,5,5]]

def job(data):
    for l in data:
        for i in range(len(l)):
            l[i]=l[i]**2
            time.sleep(1)
    return data

if __name__=="__main__":
    print(job(data))

