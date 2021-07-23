# -*- coding:utf-8 -*-

# @Time    : 2018/11/22 下午5:27

# @Author  : wangzelin

# @Email   : 1064534588@qq.com

# @File    : LRU.py

# @Project : python

# @Software: PyCharm

# @Remark  : ...
#缓存淘汰算法LRU,淘汰使用频率低的 least recently used

from collections import OrderedDict


class LRUCache1(OrderedDict):
    '''不能存储可变类型对象，不能并发访问set()'''

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if self.cache.has_key(key):
            value = self.cache.pop(key)
            self.cache[key] = value
        else:
            value = None

        return value

    def set(self, key, value):
        if self.cache.has_key(key):
            self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)  # pop出第一个item
                self.cache[key] = value
            else:
                self.cache[key] = value

c = LRUCache1(5)

for i in range(5, 10):
    c.set(i, 10 * i)

print c.cache, c.cache.keys()

c.get(5)
c.get(7)

print c.cache, c.cache.keys()

c.set(10, 100)
print c.cache, c.cache.keys()
#import pdb;pdb.set_trace()
c.set(9, 44)
print c.cache, c.cache.keys()

class LRUCache2(object):
    '''不能存储可变类型对象，不能并发访问set()'''

    def __init__(self, capacity):
        self.l = []
        self.d = {}
        self.capacity = capacity

    def get(self, key):
        if self.d.has_key(key):
            value = self.d[key]
            self.l.remove(key)
            self.l.insert(0, key)
        else:
            value = None

        return value

    def set(self, key, value):
        if self.d.has_key(key):
            self.l.remove(key)
        elif len(self.d) == self.capacity:
            oldest_key = self.l.pop()
            self.d.pop(oldest_key)

        self.d[key] = value
        self.l.insert(0, key)
import pdb;pdb.set_trace()
c = LRUCache2(5)

for i in range(5, 10):
    c.set(i, 10 * i)

print c.d, c.l

c.get(5)
c.get(7)

print c.d, c.l

c.set(10, 100)
print c.d, c.l

c.set(9, 44)
print c.d, c.l