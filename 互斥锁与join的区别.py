from threading import current_thread,Thread,Lock
import os,time

#不加锁：并发执行，速度快
# def task():
#     global n
#     print("%s is running" %current_thread().getName())
#     temp = n
#     time.sleep(0.5)
#     n = temp - 1
#
# if __name__ == '__main__':
#     n = 100
#     lock = Lock()
#     threads = []
#     start_time = time.time()
#     for i in range(100):
#         t = Thread(target=task)
#         threads.append(t)
#         t.start()
#     for t in threads:
#         t.join()
#     stop_time = time.time()
#     print("主：%s n:%s" %(stop_time-start_time,n))


#不加锁：未加锁部分并发执行，加速部分串行，速度慢，数据安全

def task():
    #未加锁的代码并发运行
    time.sleep(1)
    print("%s start to run"%current_thread().getName())
    global n
    #加锁的代码串行运行
    lock.acquire()
    temp = n
    time.sleep(0.5)
    n = temp - 1
    lock.release()

if __name__ == '__main__':

    n = 100
    lock = Lock()
    threads = []
    start_time = time.time()
    for i in range(100):
        t = Thread(target=task)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    stop_time = time.time()
    print("主：%s n:%s" %(stop_time-start_time,n))

