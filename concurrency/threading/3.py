# -*- encoding:utf-8 -*-

import threading
import time

counter = 0


class MyThread(threading.Thread):
    def __init__(self, lock):
        super(MyThread, self).__init__()
        self.lock = lock

    def run(self):
        global counter
        self.lock.acquire()
        counter += 1
        self.lock.release()

if __name__ == "__main__":
    thread_number = 1000000
    threads = []
    mutex = threading.Lock()
    st = time.time()
    for i in range(thread_number):
        t = MyThread(mutex)
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()
    et = time.time()
    print "Counter in Main thread:", counter
    print "Time used:", et-st
