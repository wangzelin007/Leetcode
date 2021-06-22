# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 1.实现入队，出队功能。
# 2.实现退出队列功能。且退出队列后需要更新队列用户位置的变化情况。
from collections import deque

class User:
    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.seq = 0

    def getName(self):
        return self.name

    def setName(self,name):
        self.name = name

    def getSeq(self):
        return self.seq

    def setSeq(self,seq):
        self.seq = seq

    def getId(self):
        return self.id

    def toString(self):
        return "id: " + str(self.id) + ", name: " + self.name + ", seq:" + str(self.seq)

class MyQueue:
    def __init__(self):
        self.q = deque() # 类似列表(list)的容器，实现了在两端快速添加(append)和弹出(pop). append/appendleft/pop/popleft

    def enQueue(self,u):
        self.q.append(u)
        u.setSeq(len(self.q))

    def deQueue(self):
        self.q.popleft()
        self.updateSeq()

    def deQueueRemove(self,u):
        self.q.remove(u) # 删除第一次出现的值
        self.updateSeq()

    def updateSeq(self):
        i = 1
        for u in self.q:
            u.setSeq(i)
            i += 1

    def printList(self):
        for u in self.q:
            print u.toString()

if __name__ == '__main__':
    u1 = User(1,"user1")
    u2 = User(2,"user2")
    u3 = User(3,"user3")
    u4 = User(4,"user4")
    q = MyQueue()
    q.enQueue(u1)
    q.enQueue(u2)
    q.enQueue(u3)
    q.enQueue(u4)
    q.deQueue()
    q.deQueueRemove(u3)
    q.printList()
    u5 = User(5,"user5")
    q.enQueue(u5)
    q.printList()