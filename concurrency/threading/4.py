# -*- encoding:utf-8 -*-

import threading

counterA = 0
counterB = 0
lockA = threading.Lock()
lockB = threading.Lock()


def funca():
    global lockA, lockB
    while True:
        lockA.acquire()
        print "func a acquire lockA"
        lockB.acquire()
        print "func a acquire lockB"
        lockB.release()
        print "func a release lockB"
        lockA.release()
        print "func a release lockA"


def funcb():
    global lockA, lockB
    while True:
        lockB.acquire()
        print "func b acquire lockB"
        lockA.acquire()
        print "func b acquire lockA"
        lockA.release()
        print "func b release lockA"
        lockB.release()
        print "func b release lockB"

if __name__ == "__main__":
    ta = threading.Thread(target=funca)
    tb = threading.Thread(target=funcb)
    ta.start()
    tb.start()
    ta.join()
    tb.join()
