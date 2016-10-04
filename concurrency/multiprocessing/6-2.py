# -*- encoding: utf-8 -*-

from multiprocessing import Pool
from requests import Session


def do_request(s):
    for i in range(100):
        r = s.get('http://localhost:8000/')
        print r.status_code, r.json()


if __name__ == "__main__":
    user_number = 6
    p = Pool(processes=user_number)
    users = [Session() for i in xrange(user_number)]
    p.map(do_request, users)
    # 停止向进程池中继续添加worker进程
    p.close()
    # 等待进程池中所有worker运行结束
    p.join()
