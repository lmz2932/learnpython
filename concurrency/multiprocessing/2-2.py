# -*- encoding: utf-8 -*-

from multiprocessing import Pipe, Process


def func(p):
    p.send([1, 'str', None])
    p.close()

# Pipe对象返回管道的两端都有send和recv方法
# 两个进程分别操作管道两端时不会有冲突
# 多进程同时操作管道一端时可能会有读写冲突
if __name__ == "__main__":
    parent_side, child_side = Pipe()
    p = Process(target=func, args=(child_side,))
    p.start()
    print parent_side.recv()
    p.join()
