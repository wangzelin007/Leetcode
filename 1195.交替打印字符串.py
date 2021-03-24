# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
from threading import *

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.curr = 0
        self.lock = [Lock() for _ in range(4)]
        self.lockAll()
        self.switchLock()

    def lockAll(self):
        for i in range(4):
            self.lock[i].acquire()

    def releaseAll(self):
        for i in range(4):
            self.lock[i].release()

    def lockAt(self, i):
        self.lock[i].acquire()

    def releaseAt(self, i):
        self.lock[i].release()

    def switchLock(self):
        self.curr += 1
        if self.curr > self.n:
            self.releaseAll()
            return

        if self.curr % 15 == 0:
            self.lock[2].release()
        elif self.curr % 3 == 0:
            self.lock[0].release()
        elif self.curr % 5 == 0:
            self.lock[1].release()
        else:
            self.lock[3].release()

    # printFizz() outputs "fizz"
    def fizz(self) -> None:
        while self.curr <= self.n:
            self.lock[0].acquire()
            if self.curr > self.n:
                continue
            print('fizz')
            self.switchLock()

    # printBuzz() outputs "buzz"
    def buzz(self) -> None:
        while self.curr <= self.n:
            self.lock[1].acquire()
            if self.curr > self.n:
                continue
            print('buzz')
            self.switchLock()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self) -> None:
        while self.curr <= self.n:
            self.lock[2].acquire()
            if self.curr > self.n:
                continue
            print('fizzbuzz')
            self.switchLock()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self) -> None:
        while self.curr <= self.n:
            self.lock[3].acquire()
            if self.curr > self.n:
                continue
            print(self.curr)
            self.switchLock()

if __name__ == '__main__':
    n = 30
    foo = FizzBuzz(n)
    # for i in range(n):
    Threads = []
    t1 = Thread(target=foo.buzz, args=())
    t2 = Thread(target=foo.fizz, args=())
    t3 = Thread(target=foo.fizzbuzz, args=())
    t4 = Thread(target=foo.number, args=())
    t1.setDaemon(True)
    t2.setDaemon(True)
    t3.setDaemon(True)
    t4.setDaemon(True)
    Threads.extend([t1, t2, t3, t4])
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    for t in Threads:
        t.join()