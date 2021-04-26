# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
import queue
import logging
from threading import *

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

def printFoo(count=None):
    logging.debug("foo,{}".format(count))

def printBar(count=None):
    logging.debug("bar,{}".format((count)))

# semaphore 推荐解法
# 也是生产者、消费者 基本模型
class FooBar2(object):
    def __init__(self, n):
        self.n = n
        self.fs = Semaphore(1)
        self.bs = Semaphore(0)
        self.fc = 1
        self.bc = 1

    def foo(self, printFoo):
        for i in range(self.n):
            self.fs.acquire()
            printFoo(self.fc)
            self.bs.release()
            self.fc += 1

    def bar(self, printBar):
        for i in range(self.n):
            self.bs.acquire()
            printBar(self.bc)
            self.fs.release()
            self.bc += 1

# queue
class FooBar1(object):
    def __init__(self, n):
        self.n = n
        self.q = queue.Queue(1)
        self.fc = 1
        self.bc = 1

    def foo(self, printFoo):
        for i in range(self.n):
            self.q.put(0)
            printFoo(self.fc)
            self.fc += 1

    def bar(self, print):
        for i in range(self.n):
            self.q.get()
            printBar(self.bc)
            self.bc += 1

# condition
class FooBar4:
    def __init__(self, n):
        self.n = n
        self.c = Condition()
        self.t = 0
        self.fc = 1
        self.bc = 1

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.res(0, printFoo)

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.res(1, printBar)

    def res(self, value: int, func: 'Callable[[], None]') -> None:
        with self.c:
            self.c.wait_for(lambda: value == self.t)
            if self.t == 0:
                func(self.fc)
                self.t += 1
                self.fc += 1
            else:
                func(self.bc)
                self.t -= 1
                self.bc += 1
            self.c.notify_all()

# lock
class FooBar5:
    def __init__(self, n):
        self.n = n
        self.fl = Lock()
        self.bl = Lock()
        self.bl.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            with self.fl:
                printFoo()
                self.bl.release()
                self.fl.acquire()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            with self.bl:
                printBar()
                self.fl.release()
                self.bl.acquire()

if __name__ == '__main__':
    fun = FooBar5(100)
    import threading
    threads = []
    thread1 = threading.Thread(target=fun.foo, args=(printFoo,))
    threads.append(thread1)
    thread1.setDaemon(True)
    thread1.start()
    thread2 = threading.Thread(target=fun.bar, args=(printBar,))
    threads.append(thread2)
    thread2.setDaemon(True)
    thread2.start()
    for t in threads:
        t.join()