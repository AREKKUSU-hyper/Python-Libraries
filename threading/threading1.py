import threading
def thread_job():
    print("This is an added Thread, number is %s" % threading.current_thread())

def main():
    added_thread=threading.Thread(target=thread_job)
    # print(threading.current_thread())
    added_thread.start()
    print(threading.active_count())
    print(threading.enumerate())

if __name__=="__main__":
    main()
