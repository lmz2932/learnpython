# -*- encoding: utf-8 -*-

from threading import Thread
import time


def func():
    print "Child thread start, %s" % time.ctime()
    time.sleep(2)
    print "Child thread end, %s" % time.ctime()


if __name__ == "__main__":
    print "Parent thread start, %s" % time.ctime()
    p = Thread(target=func)
    # 开始执行子线程
    p.start()
    # 等待子线程结束
    p.join()
    time.sleep(1)
    print "Parent thread end, %s" % time.ctime()
