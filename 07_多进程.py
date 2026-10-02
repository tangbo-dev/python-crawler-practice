from multiprocessing import Process  # 进程
from threading import Thread    # 线程



def work():
    for i in range(10000):
        print("子进程", i)


if __name__ == '__main__':
    p = Process(target=work)
    p.start()
    # 进程的开销是比较大的...
    for i in range(100000):
        print("主进程", i)


