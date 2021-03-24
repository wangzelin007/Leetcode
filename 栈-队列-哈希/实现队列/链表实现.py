# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# enQueue： cur.next
# deQueue：head.next = head.next.next
# isEmpty size getFront getBack
class LNode:
    def __new__(self, x):
        self.data = x
        self.next = None

class MyQueue:
    def __init__(self):
        self.head = None
        self.end = None

    def isEmpty(self):
        return False if self.head else True

    def size(self):
        size = 0
        tmp = self.head
        if tmp:
            size += 1
            tmp = tmp.next
        return size

    def getFront(self):
        return self.head.data if self.head else None

    def getBack(self):
        return self.end.data if self.end else None

    def enQueue(self, x):
        p = LNode
        p.data = x
        p.next = None
        if not self.head:
            self.head = self.end = p
        else:
            self.end.next = p
            self.end = p

    def deQueue(self):
        if not self.head:
            return None
        self.head = self.head.next
        if self.head is None:
            self.end = None

if __name__ == '__main__':
    q = MyQueue()
    print(q.isEmpty())
    print(q.size())
    print(q.getFront())
    print(q.getBack())
    q.enQueue(1)
    print(q.isEmpty())
    print(q.size())
    print(q.getFront())
    print(q.getBack())
    q.deQueue()
    print(q.isEmpty())