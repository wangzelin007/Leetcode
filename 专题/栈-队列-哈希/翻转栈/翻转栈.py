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
        # 显示栈顶元素
        if not self.isEmpty():
            return self.items[len(self.items)-1]
        else:
            return None

    def pop(self):
        if not self.isEmpty():
            self.items.pop()
        else:
            return None

    def push(self, x):
        self.items.append(x)

def moveBottomToTop(s):
    if s.isEmpty():
        return
    # 栈顶元素
    top1 = s.peek()
    s.pop()
    if not s.isEmpty():
        moveBottomToTop(s)
        # 子栈顶元素
        top2 = s.peek()
        s.pop()
        s.push(top1)
        s.push(top2)
    else:
        s.push(top1)

def reverse_stack(s):
    if s.isEmpty():
        return
    moveBottomToTop(s)
    top = s.peek()
    s.pop()
    reverse_stack(s)
    s.push(top)

if __name__ == '__main__':
    s = Stack()
    s.push(5)
    s.push(4)
    s.push(3)
    s.push(2)
    s.push(1)
    # 1 2 3 4 5
    reverse_stack(s)
    while not s.isEmpty():
        print s.peek(),
        s.pop()
