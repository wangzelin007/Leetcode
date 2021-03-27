# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 仅入栈 A
# 出栈：
# 1.如果B不为空，B.pop()
# 2.B为空，while A.notEmpty(A.pop() && B.push) B.pop()
class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def empty(self):
        return self.size() == 0

    def peek(self):
        if not self.empty():
            return self.items[self.size()-1]
        else:
            return None

    def push(self,x):
        self.items.append(x)

    def pop(self):
        if not self.empty():
            return self.items.pop()
        else:
            return None

class MyStack:
    def __init__(self):
        self.ins = Stack()
        self.outs = Stack()

    def push(self,x):
        self.ins.push(x)

    def pop(self):
        if self.outs.empty():
            while not self.ins.empty():
                self.outs.push(self.ins.pop())
        return self.outs.pop()

if __name__ == '__main__':
    s = MyStack()
    s.push(1)
    s.push(2)
    print(s.pop()) # 1
    s.push(3)
    print(s.pop()) # 2
    print(s.pop()) # 3
    print(s.pop()) # None