# -*- encoding: utf-8 -*-

from multiprocessing import Queue, Process


def func(q):
    q.put([1, 'str', None])

# Queue是进程及线程安全的
if __name__ == "__main__":
    q = Queue()
    p = Process(target=func, args=(q,))
    p.start()
    p.join()
    print q.get()
