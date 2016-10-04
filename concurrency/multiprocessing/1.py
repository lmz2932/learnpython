# -*- encoding: utf-8 -*-

from multiprocessing import Process
import os


def get_process(info):
    print info
    # *nix系统才有getpid及getppid方法
    print 'Process ID:', os.getpid()
    print 'Parent process ID:', os.getppid()


def func(name):
    get_process('In func:')
    print "Hello,", name


if __name__ == "__main__":
    get_process('In main:')
    p = Process(target=func, args=('marsloo',))
    # 开始子进程
    p.start()
    # 等待子进程结束
    p.join()
