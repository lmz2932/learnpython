# -*- encoding: utf-8 -*-

from multiprocessing import Process, Value, Array


def func(n, a):
    n.value = 3.1415926
    for i in range(len(a)):
        a[i] = -i


if __name__ == "__main__":
    # 使用共享内存，共享内存是线程安全的
    # 'd'表示浮点型数据，'i'表示整数
    n = Value('d', 0.0)
    a = Array('i', range(10))
    p = Process(target=func, args=(n, a,))
    p.start()
    p.join()

    print n.value
    print a[:]
