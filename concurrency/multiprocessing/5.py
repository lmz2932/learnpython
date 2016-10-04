# -*- encoding: utf-8 -*-

from multiprocessing import Pool, TimeoutError
import os
import time


def func(x):
    return x * x

if __name__ == "__main__":
    p = Pool(processes=4)

    print p.map(func, range(10))

    for r in p.imap_unordered(func, range(10)):
        print r,
    print

    # 异步执行
    res = p.apply_async(func, (20,))
    print res.get(timeout=1)

    res = p.apply_async(os.getpid, ())
    print res.get(timeout=1)

    resutls = [p.apply_async(os.getpid, ()) for i in range(4)]
    print [r.get(timeout=1) for r in resutls]

    res = p.apply_async(time.sleep, (3,))
    try:
        print res.get(timeout=1)
    except TimeoutError:
        print "Timeout error!"
