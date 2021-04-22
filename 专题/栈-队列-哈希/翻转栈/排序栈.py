# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.items[self.size()-1]

    def push(self,x):
        self.items.append(x)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            self.items.pop()

def MoveMaxToTop(s):
    if s.isEmpty():
        return
    top1 = s.peek()
    s.pop()
    if not s.isEmpty():
        MoveMaxToTop(s)
        top2 = s.peek()
        if top1 < top2:
            s.pop()
            s.push(top1)
            s.push(top2)
            return
    s.push(top1)



def reverse(s):
    if s.isEmpty():
        return
    MoveMaxToTop(s)
    top = s.peek()
    s.pop()
    reverse(s)
    s.push(top)

if __name__ == '__main__':
    s = Stack()
    # 2 3 1
    s.push(1)
    s.push(3)
    s.push(2)
    reverse(s)
    while not s.isEmpty():
        print s.peek(),
        s.pop()
    # 3 2 1