# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 要求：时间复杂度O(1)
# 用空间换时间，如果小于 s2.peek，执行s2.push 操作，最后返回 s2.peek
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.isEmpty():
            return self.items[self.size()-1]
        else:
            return None

    def push(self,x):
        self.items.append(x)

    def pop(self):
        if not self.isEmpty():
            self.items.pop()
        else:
            return None

class MyStack:
    def __init__(self):
        self.s = Stack()
        self.m = Stack()

    def pop(self):
        if self.s.isEmpty():
            return None
        top = self.s.peek()
        self.s.pop()
        if top == self.mins():
            self.m.pop()
        return top

    def push(self,x):
        self.s.push(x)
        if self.m.isEmpty():
            self.m.push(x)
        elif x <= self.m.peek():
            self.m.push(x)

    def mins(self):
        if self.m.isEmpty():
            return None
        else:
            return self.m.peek()

if __name__ == '__main__':
    s = MyStack()
    # 4 5 1 2 3
    s.push(3)
    print(s.mins())
    s.push(2)
    print(s.mins())
    s.push(1)
    print(s.mins())
    s.push(5)
    print(s.mins())
    s.push(4)
    print(s.mins())
    s.push(0)
    print(s.mins())
    print '\n'
    s.pop()
    print(s.mins())
    s.pop()
    print(s.mins())
    s.pop()
    print(s.mins())
    s.pop()
    print(s.mins())
    s.pop()
    print(s.mins())
    s.pop()
    print(s.mins())