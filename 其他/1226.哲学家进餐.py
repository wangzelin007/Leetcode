# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
from threading import *
# from multiprocessing import Process as Thread

class DiningPhilosophers():
    """
    output[i] = [a, b, c]
    a 哲学家编号
    b 叉子 1 左边 2 右边
    c 行为 1 拿起 2 放下 3 吃面
    """
    def __init__(self):
        self.f = [Lock() for _ in range(5)]

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        while True:
            if self.f[philosopher].acquire(timeout=0.001):
                if philosopher != 4:
                    if self.f[philosopher+1].acquire(timeout=0.001):
                        pickLeftFork(philosopher)
                        pickRightFork(philosopher)
                    else:
                        self.f[philosopher].release()
                        continue
                else:
                    if self.f[0].acquire(timeout=0.001):
                        pickLeftFork(philosopher)
                        pickRightFork(philosopher)
                    else:
                        self.f[philosopher].release()
                        continue
            else:
                continue
            eat(philosopher)
            putLeftFork(philosopher)
            self.f[philosopher].release()
            putRightFork(philosopher)
            if philosopher != 4:
                self.f[philosopher+1].release()
            else:
                self.f[0].release()
            break

list = []

def pickLeftFork(philosopher):
    list.append([philosopher, 1, 1])

def pickRightFork(philosopher):
    list.append([philosopher, 2, 1])

def eat(philosopher):
    import time
    time.sleep(1)
    list.append([philosopher, 0, 3])

def putLeftFork(philosopher):
    list.append([philosopher, 1, 2])

def putRightFork(philosopher):
    list.append([philosopher, 2, 2])

if __name__ == '__main__':
    foo = DiningPhilosophers()
    threads = []
    for i in range(4):
        thread0 = Thread(target=foo.wantsToEat, args=(0, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork))
        thread1 = Thread(target=foo.wantsToEat, args=(1, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork))
        thread2 = Thread(target=foo.wantsToEat, args=(2, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork))
        thread3 = Thread(target=foo.wantsToEat, args=(3, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork))
        thread4 = Thread(target=foo.wantsToEat, args=(4, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork))
        threads.extend([thread0, thread1, thread2, thread3, thread4])
        thread0.setDaemon(True)
        thread1.setDaemon(True)
        thread2.setDaemon(True)
        thread3.setDaemon(True)
        thread4.setDaemon(True)

        thread0.start()
        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        for t in threads:
            t.join()
    print(list)
    print(len(list))