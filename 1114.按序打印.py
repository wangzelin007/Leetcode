# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
import queue

class Foo(object):
    def __init__(self):
        self.q = queue.Queue(1)
        self.r = queue.Queue(1)

    def first(self):
        """
        :type printFirst: method
        :rtype: void
        """
        # printFirst() outputs "first". Do not change or remove this line.
        print('First')
        self.q.put(0)

    def second(self):
        """
        :type printSecond: method
        :rtype: void
        """
        self.q.get()
        # printSecond() outputs "second". Do not change or remove this line.
        print('Second')
        self.r.put(0)

    def third(self):
        """
        :type printThird: method
        :rtype: void
        """
        self.r.get()
        # printThird() outputs "third". Do not change or remove this line.
        print('Third')


if __name__ == '__main__':
    foo = Foo()
    myDict = {"A": foo.first,
              "B": foo.second,
              "C": foo.third}
    from random import sample
    myList = sample(['A', 'B', 'C'], k=3)
    import threading
    threads = []
    for i in myList:
        t_name = 'thread' + i
        t_name = threading.Thread(target=myDict[i], args=())
        threads.append(t_name)
        t_name.setDaemon(True)
        t_name.start()
    for t in threads:
        t.join()

