# -*- encoding:utf-8 -*-

import threading

counterA = 0

lock = threading.RLock()
# 如果使用普通互斥锁，会造成死锁
# lock = threading.Lock()


def func():
    global lock

    lock.acquire()
    print "I acquire lock"
    lock.acquire()
    print "I acquire lock again"
    lock.release()
    print "I release lock again"
    lock.release()
    print "I release lock"


if __name__ == "__main__":
    t = threading.Thread(target=func)
    t.start()
    t.join()
