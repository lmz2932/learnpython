# -*- encoding: utf-8 -*-

from multiprocessing import Process

a = [2]


def func(i):
    global a
    a[i] += 1
    print "a[0] in child prcocess:", a[0]

if __name__ == "__main__":
    p = Process(target=func, args=(0, ))
    p.start()
    p.join()
    print "a[0] in parent process:", a[0]

# 进程间的内存空间是不共享的，即使是全局变量
# 在进程间共享状态必须使用共享内存或服务进程

# 程序输出
# a[0] in child prcocess: 3
# a[0] in parent process: 2
