# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
import threading

class ZeroEvenOdd:
    s = [threading.Semaphore(0), threading.Semaphore(0), threading.Semaphore(1)]
    def __init__(self, n):
        self.n = n

	# printNumber(x) outputs "x", where x is an integer.
    def zero(self):
        for i in range(self.n):
            self.s[2].acquire()
            print(0);
            self.s[i%2].release()

    def odd(self):
        for i in range(1, self.n+1, 2):
            self.s[0].acquire()
            print(i)
            self.s[2].release()

    def even(self):
        for i in range(2, self.n+1, 2):
            self.s[1].acquire()
            print(i)
            self.s[2].release()

if __name__ == '__main__':
    n = 5
    foo = ZeroEvenOdd(n)
    from threading import *
    theardA = Thread(target=foo.zero, args=())
    theardB = Thread(target=foo.even, args=())
    theardC = Thread(target=foo.odd, args=())
    theards = [theardA, theardB, theardC]
    theardA.setDaemon(True)
    theardB.setDaemon(True)
    theardC.setDaemon(True)
    theardA.start()
    theardB.start()
    theardC.start()
    for t in theards:
        t.join()