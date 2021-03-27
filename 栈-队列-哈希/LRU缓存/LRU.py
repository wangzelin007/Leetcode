# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
from collections import deque

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
        print self.hash.get(key, -1)

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

if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)        # 返回  1
    cache.put(3, 3)     # 该操作会使得密钥 2 作废
    cache.get(2)        # 返回 -1 (未找到)
    cache.put(4, 4)     # 该操作会使得密钥 1 作废
    cache.get(1)        # 返回 -1 (未找到)
    cache.get(3)        # 返回  3
    cache.get(4)        # 返回  4
