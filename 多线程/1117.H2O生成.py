# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
from threading import *
from collections import *

class H2O:
    def __init__(self):
        self.h = deque()
        self.o = self.h.copy()

    def hydrogen(self):
        self.h.append(self.printh)
        self.res()
        # releaseHydrogen() outputs "H". Do not change or remove this line.

    def oxygen(self):
        # releaseOxygen() outputs "O". Do not change or remove this line.
        self.o.append(self.printo)
        self.res()

    def printh(self):
        print('H')

    def printo(self):
        print('O')

    def res(self):
        if len(self.h) > 1 and len(self.o) > 0:
            self.h.popleft()()
            self.h.popleft()()
            self.o.popleft()()


if __name__ == '__main__':
    foo = H2O()
    name = list('OOHHHH')
    print(name)
    threads = []
    for i in name:
        t_name = 'thread' + i
        if i == 'H':
            t_name = Thread(target=foo.hydrogen, args=())
            threads.append(t_name)
            t_name.setDaemon(True)
            t_name.start()
        else:
            t_name = Thread(target=foo.oxygen, args=())
            threads.append(t_name)
            t_name.setDaemon(True)
            t_name.start()
    for t in threads:
        t.join()
