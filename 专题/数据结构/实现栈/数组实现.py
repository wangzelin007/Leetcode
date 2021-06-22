# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
class MyStack:
    # 模拟栈
    def __init__(self):
        self.items = []
    # 判断栈是否为空
    def isEmpty(self):
        return len(self.items) == 0
    # 返回栈的大小
    def size(self):
        return len(self.items)
    # 返回栈顶元素
    def top(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None
    # 弹栈
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print('Empty, can not pop')
            return None
    # 压栈
    def push(self, x):
        self.items.append(x)

if __name__ == '__main__':
    s = MyStack()
    s.push(4)
    print(s.top())
    print(s.size())
    print(s.isEmpty())
    print(s.pop())
    print(s.isEmpty())
    print(s.top())
    print(s.pop())