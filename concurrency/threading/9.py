# -*- encoding: utf-8 -*-

import threading
import time


def func():
    print "%s I started" % time.ctime()

if __name__ == "__main__":
    print "%s Program started" % time.ctime()
    t = threading.Timer(3.0, func)
    t.start()
    # 如果定时器在等待阶段被cancel，则其绑定的函数不会被执行
    # time.sleep(2)
    # t.cancel()
