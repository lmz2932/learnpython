# -*- encoding: utf-8 -*-

import threading
import time

e = threading.Event()


def funcx():
    print "%s X is restarting ..." % time.ctime()
    time.sleep(3)
    # 底层被依赖线程重启3秒后置位为True
    e.set()
    print "%s X restarted" % time.ctime()


def func():
    # 循环检测，直到底层服务重启完成
    while not e.is_set():
        print "%s waiting for X ..." % time.ctime()
        # 如果底层服务未重启完成，阻塞最多等待1秒
        e.wait(1)
    # 底层服务重启完成后开始工作
    print "%s %s start working ..." % (time.ctime(),
                                       threading.current_thread().name)


if __name__ == "__main__":
    x = threading.Thread(target=funcx)
    abc = [threading.Thread(target=func) for i in xrange(3)]
    x.start()
    for t in abc:
        t.start()
    x.join()
    for t in abc:
        t.join()
    print "Existing..."
    # 退出前将Event置位为False
    e.clear()
