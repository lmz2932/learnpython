from multiprocessing import Manager, Process, Lock


def func(d, l):
    l.acquire()
    d.value += 1
    l.release()

if __name__ == "__main__":
    l = Lock()
    m = Manager()
    d = m.Value('d', 0)

    pids = []
    for i in range(10000):
        p = Process(target=func, args=(d, l, ))
        pids.append(p)
        p.start()

    for pid in pids:
        pid.join()

    # 如果没有加锁，最后的值可能会小于10000
    print d.value
