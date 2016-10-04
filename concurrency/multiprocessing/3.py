# -*- encoding: utf-8 -*-

from multiprocessing import Lock, Process


def lock_func(l, number):
    l.acquire()
    print "Number is: %d" % number
    l.release()


if __name__ == "__main__":
    # 没有锁，终端输出可能会错乱
    l = Lock()
    for number in range(10):
        Process(target=lock_func, args=(l, number,)).start()
