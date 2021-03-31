# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# import queue
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

# queue
# class FooBar(object):
#     def __init__(self, n):
#         self.n = n
#         self.q = queue.Queue(1)
#         logging.debug(self.n)
#
#     def foo(self):
#         """
#         :type printFoo: method
#         :rtype: void
#         """
#         count = 1
#         for i in range(self.n):
#             self.q.put(0)
#             # printFoo() outputs "foo". Do not change or remove this line.
#             logging.debug("foo,{}".format(count))
#             count += 1
#
#     def bar(self):
#         """
#         :type printBar: method
#         :rtype: void
#         """
#         count = 1
#         for i in range(self.n):
#             self.q.get()
#             # printBar() outputs "bar". Do not change or remove this line.
#             logging.debug("bar,{}".format(count))
#             count += 1

#semaphore py2 && py3
from threading import *


class FooBar(object):
    def __init__(self, n):
        self.n = n
        self.fs = Semaphore(1)
        self.bs = Semaphore(0)
        logging.debug(self.n)

    def foo(self):
        """
        :type printFoo: method
        :rtype: void
        """
        count = 1
        for i in range(self.n):
            self.fs.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            logging.debug("foo,{}".format(count))
            self.bs.release()
            count += 1

    def bar(self):
        """
        :type printBar: method
        :rtype: void
        """
        count = 1
        for i in range(self.n):
            self.bs.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            logging.debug("bar,{}".format(count))
            self.fs.release()
            count += 1

if __name__ == '__main__':
    fun = FooBar(100)
    import threading
    threads = []
    thread1 = threading.Thread(target=fun.foo, args=())
    threads.append(thread1)
    thread1.setDaemon(True)
    thread1.start()
    thread2 = threading.Thread(target=fun.bar, args=())
    threads.append(thread2)
    thread2.setDaemon(True)
    thread2.start()
    for t in threads:
        t.join()
    # fun.foo()
    # fun.bar()
    # import time
    # time.sleep(30)