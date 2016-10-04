# -*- encoding: utf-8 -*-

import multiprocessing as mp
from requests import Session


def do_request(s):
    for i in range(100):
        r = s.get('http://localhost:8000/')
        print r.status_code, r.json()


if __name__ == "__main__":
    user_number = 6
    users = [Session() for i in xrange(user_number)]
    jobs = []

    for user in users:
        p = mp.Process(target=do_request, args=(user,))
        jobs.append(p)
        p.start()

    for user in users:
        user.join()
