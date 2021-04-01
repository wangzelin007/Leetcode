# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )
#
# 示例 1：
# 输入：
# ["CQueue","appendTail","deleteHead","deleteHead"]
# [[],[3],[],[]]
# 输出：[null,null,3,-1]
#
# 示例 2：
# 输入：
# ["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
# [[],[],[5],[2],[],[]]
# 输出：[null,-1,null,null,5,2]
class CQueue(object):

    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.inStack.push(value)

    def deleteHead(self):
        """
        :rtype: int
        """
        if self.outStack.isEmpty():
            while not self.inStack.isEmpty():
                self.outStack.push(self.inStack.pop())
        return self.outStack.pop()

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def push(self,x):
        self.items.append(x)

    def pop(self):
        if not self.isEmpty(): return self.items.pop()
        else: return -1

    def peek(self):
        if not self.isEmpty(): return self.items[-1]
        else: return -1

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
if __name__ == '__main__':
    c = CQueue()
    print(c.appendTail(5))
    print(c.appendTail(2))
    print(c.deleteHead())
    print(c.deleteHead())
    # s = Stack()
    # print(s.push(5))
    # print(s.pop())
    # print(s.isEmpty())