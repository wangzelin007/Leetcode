# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
#head 1 2 3 4 5 6 7 8
#head 2 1 3 4 5 6 7 8
#head 2 1 4 3 5 6 7 8
#head 2 1 4 3 6 5 7 8
import random

class LNode(object):
    def __init__(self,x):
        self.data = x
        self.next = None

def createLinkedList(l):
    head = LNode(None)
    cur = head
    i = 1
    while i <= l:
        n = random.randint(0, 9)
        tmp = LNode(n)
        cur.next = tmp
        cur = tmp
        i += 1
    return head

def printLinkedList(head):
    cur = head.next
    while cur is not None:
        print(cur.data, end=',')
        cur = cur.next

def printLinkedList2(head):
    cur = head
    while cur is not None:
        print(cur.data, end=',')
        cur = cur.next

# 有头
def switch(head):
    if head is None or head.next is None:
        return
    pre = head
    cur = head.next
    next = None
    while cur is not None and cur.next is not None:
        next = cur.next.next # 定位next 3
        cur.next.next = cur # 2>1
        pre.next = cur.next # head>2
        cur.next = next #1>3
        pre = cur
        cur = next

# 无头
class Solution:
    def switchPairs(self, head):
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, a.next, b.next = b, b.next, a
            pre = a
        return self.next

if __name__ == '__main__':
    head = createLinkedList(8)
    from copy import deepcopy
    head2 = deepcopy(head)
    print('\n')
    printLinkedList(head)
    switch(head)
    print('\n')
    printLinkedList(head)
    s = Solution()
    head2 = head2.next
    print('\n')
    printLinkedList2(head2)
    head2 = s.switchPairs(head2)
    print('\n')
    printLinkedList2(head2)
