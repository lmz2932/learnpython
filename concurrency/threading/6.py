# -*- encoding: utf-8 -*-

import threading

products = 0
c = threading.Condition()


class Producer(threading.Thread):
    def __init__(self):
        super(Producer, self).__init__()

    def run(self):
        global products, c
        while True:
            # 获取条件对象锁
            c.acquire()
            if products >= 10:
                print "Enough products.."
                # 进入等待池等待重新获取锁，但是不自动释放已经获得的锁
                c.wait()
            else:
                products += 1
                print "Produce 1 product, now we have %d \
                        product(s)." % products
                # 在等待池内选一个对象通知其重新获取锁
                # 但是不自动释放已经获得的锁
                c.notify()
            # 主动释放条件对象锁
            c.release()


class Consumer(threading.Thread):
    def __init__(self):
        super(Consumer, self).__init__()

    def run(self):
        global products, c
        while True:
            c.acquire()
            if products <= 2:
                print "Low inventory.."
                c.wait()
            else:
                products -= 1
                print "Consum 1 product, now we have %d product(s)." % products
                c.notify()
            c.release()

if __name__ == "__main__":
    producer_number = 4
    consumer_number = 5
    producers = [Producer() for i in xrange(producer_number)]
    consumers = [Consumer() for i in xrange(consumer_number)]
    for producer in producers:
        producer.start()
    for consumer in consumers:
        consumer.start()
