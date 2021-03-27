# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 递归一
# 结束条件只有一个元素
# 1.将栈底元素 移动到 栈顶
# 2.拿掉栈顶元素
# 3.返回时将栈顶元素加回栈顶
# 递归二 是递归一 步骤一的分解
# 结束条件 只有一个元素
# 1.递归处理
# 2.将栈顶元素和子栈顶元素交换位置
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

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

def moveBottomToTop(s):
    if s.isEmpty():
        return
    top1 = s.peek()
    s.pop()
    if not s.isEmpty():
        moveBottomToTop(s)
        top2 = s.peek()
        s.pop()
        s.push(top1)
        s.push(top2)
    else:
        s.push(top1)

def reverse(s):
    if s.isEmpty():
        return
    moveBottomToTop(s)
    top = s.peek()
    s.pop()
    reverse(s)
    s.push(top)

if __name__ == '__main__':
    s = Stack()
    s.push(5)
    s.push(4)
    s.push(3)
    s.push(2)
    s.push(1)
    reverse(s)
    while not s.isEmpty():
        print s.peek(),
        s.pop()