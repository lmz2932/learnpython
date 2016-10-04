# -*- encoding: utf-8 -*-

from multiprocessing import Process, Manager


def func(d, l):
    d['1'] = 2
    d[2] = 'str'
    d[3.0] = None
    for i in range(len(l)):
        l[i] = -i


if __name__ == "__main__":
    # Manager对象像是一个保存状态的代理
    # 其他进程通过与代理的接口通信取得状态信息
    # 服务进程支持更多的数据类型，使用起来比共享内存更灵活
    m = Manager()
    l = m.list(range(10))
    d = m.dict()
    p = Process(target=func, args=(d, l,))
    p.start()
    p.join()

    print d
    print l
