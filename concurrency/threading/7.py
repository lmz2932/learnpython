# -*- encoding: utf-8 -*-

import threading
import time
import random

s = threading.Semaphore(3)


def func():
    while True:
        s.acquire()
        name = threading.current_thread().name
        st = random.choice([0.1, 0.2, 0.3])
        print "%s will sleep %f seconds.." % (name, st)
        time.sleep(st)
        s.release()

if __name__ == "__main__":
    user_number = 6
    users = [threading.Thread(target=func) for i in xrange(user_number)]
    for user in users:
        user.start()
