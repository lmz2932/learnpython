# -*- encoding: utf-8 -*-

import threading
import time


def func():
    print "Child thread name:", threading.current_thread().name
    print "Child thread start, %s" % time.ctime()
    time.sleep(2)
    print "Child thread end, %s" % time.ctime()


if __name__ == "__main__":
    print "Parent thread name:", threading.current_thread().name
    print "Parent thread start, %s" % time.ctime()
    p = threading.Thread(target=func)
    # 设置为守护线程
    p.daemon = True
    # 开始执行子线程
    p.start()
    time.sleep(1)
    print "Parent thread end, %s" % time.ctime()
