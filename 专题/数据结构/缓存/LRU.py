# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
from collections import deque
from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.size = capacity
        self.q = deque()
        self.hash = dict()


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hash:
            self.q.remove(key)
            self.q.appendleft(key)
        return self.hash.get(key, -1)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.hash:
            self.q.remove(key)
        else:
            if len(self.q) == self.size:
                key1 = self.q.pop()
                self.hash.pop(key1)
        self.q.appendleft(key)
        self.hash[key] = value

class LRUCache2(object):

    def __init__(self, capacity):
        self.hash = OrderedDict()
        self.remain = capacity

    def get(self, key):
        if key not in self.hash:
            return -1
        v = self.hash.pop(key)
        self.hash[key] = v
        return v

    def put(self, key, value):
        if key in self.hash:
            self.hash.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                # last = False means FIFO remove
                self.hash.popitem(last=False)
        self.hash[key] = value

if __name__ == '__main__':
    cache1 = LRUCache(2)
    cache2 = LRUCache2(2)
    cache1.put(1, 1); cache2.put(1, 1)
    cache1.put(2, 2); cache2.put(2, 2)
    assert cache1.get(1) == cache2.get(1)       # 返回  1
    cache1.put(3, 3); cache2.put(3, 3)          # 该操作会使得密钥 2 作废
    assert cache1.get(2) == cache2.get(2)       # 返回 -1 (未找到)
    cache1.put(4, 4); cache2.put(4, 4)          # 该操作会使得密钥 1 作废
    assert cache1.get(1) == cache2.get(1)       # 返回 -1 (未找到)
    assert cache1.get(3) == cache2.get(3)       # 返回  3
    assert cache1.get(4) == cache2.get(4)       # 返回  4
