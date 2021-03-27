# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 1. 入栈到元素 等于 出栈序列的当前元素
# 2. 执行出栈到 栈顶不等于 出栈序列的当前元素
# 3. 继续执行入栈，直到入栈执行完毕。
# 3.1 出栈序列未全部遍历，且栈顶元素不等于不等于出栈序列的当前元素，即不是出栈序列
# 3.2 出栈序列全部遍历完成，且栈为空，即可能是出栈序列。
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
            self.items.pop()
        else:
            return None

def isPopSerial(push,pop):
    if not push or not pop:
        return False
    if len(push) != len(pop):
        return False
    s = Stack()
    while push:
        s.push(push[0])
        push = push[1:]
        while pop and s.peek() == pop[0]:
            s.pop()
            pop = pop[1:]
    if not pop and s.isEmpty():
        return True
    else:
        return False

if __name__ == '__main__':
    push = '12345'
    pop = '32541'
    pop2 = '53412'
    pop3 = '5'
    pop4 = '54321'
    pop5 = '43215'
    pop6 = '32145'
    pop7 = '32154'
    pop8 = '21534'
    print(isPopSerial(push, pop))
    print(isPopSerial(push, pop2))
    print(isPopSerial(push, pop3))
    print(isPopSerial(push, pop4))
    print(isPopSerial(push, pop5))
    print(isPopSerial(push, pop6))
    print(isPopSerial(push, pop7))
    print(isPopSerial(push, pop8))
