# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 缺点，链表很长时，即数字超出了long的表示范围时会失效。
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
        n = random.randint(0,9)
        tmp = LNode(n)
        cur.next = tmp
        cur = tmp
        i += 1
    return head

def printLinkedList(head):
    cur = head.next
    while cur is not None:
        print cur.data,
        cur = cur.next

def addLinkedList(l1, l2):
    cur1 = l1.next
    cur2 = l2.next
    x1 = []
    x2 = []
    while cur1 is not None:
        x1.append(cur1.data)
        cur1 = cur1.next
    while cur2 is not None:
        x2.append(cur2.data)
        cur2 = cur2.next
    x1.reverse()
    x2.reverse()
    return int("".join([str(i) for i in x1])) + \
           int("".join([str(i) for i in x2]))

if __name__ == '__main__':
    LinkedList1 = createLinkedList(8)
    printLinkedList(LinkedList1)
    print '\n'
    LinkedList2 = createLinkedList(8)
    printLinkedList(LinkedList2)
    print '\n'
    print(addLinkedList(LinkedList1, LinkedList2))

