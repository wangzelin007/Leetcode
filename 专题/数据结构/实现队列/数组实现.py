# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 队列 先进先出 后进后出
# 队列 空否 长度 头 尾
# 出队 head.next = head.next.next
# 入队 cur.next
# getFront getBack deQueue enQueue
class MyQueue:
    def __init__(self):
        self.arr = []
        self.front = 0 # 队列头
        self.rear = 0 # 队列尾

    def isEmpty(self):
        return self.front == self.rear

    def size(self):
        return self.rear - self.front

    def getFront(self):
        if self.isEmpty():
            return None
        else:
            return self.arr[self.front]

    def getBack(self):
        if self.isEmpty():
            return None
        else:
            return self.arr[self.rear - 1]

    def deQueue(self):
        if self.rear > self.front:
            self.front += 1
        else:
            return None

    def enQueue(self, x):
        self.arr.append(x)
        self.rear += 1

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
    print(q.size())
