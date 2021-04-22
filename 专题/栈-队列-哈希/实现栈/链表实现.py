# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 先进后出，后进先出
# 入栈 在 head 后面插入
# 出栈 head.next = head.next.next
class LNode:
    def __new__(self, x):
        self.data = x
        self.next = None

class MyStack:
    def __init__(self):
        self.data = None
        self.next = None

    def isEmpty(self):
        if self.next is None:
            return True
        else:
            return False

    def size(self):
        size = 0
        cur = self.next
        while cur:
            size += 1
            cur = cur.next
        return size

    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.next.data

    def push(self, x):
        p = LNode
        p.data = x
        p.next = self.next
        self.next = p

    def pop(self):
        tmp = self.next
        if tmp:
            self.next = tmp.next
            return tmp.data
        else:
            return None

if __name__ == '__main__':
    stack = MyStack()
    print(stack.size())
    stack.push(4)
    print(stack.size())
    print(stack.top())
    print(stack.isEmpty())
    print(stack.pop())
    print(stack.isEmpty())
    print(stack.top())
    print(stack.pop())
