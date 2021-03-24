# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 1.查找K+1位置的slow 和fast
# 2.切断链表
# 3.重组
import random

class LNode(object):
    def __init__(self,x):
        self.data = x
        self.next = None

def createLinkedList(l):
    head = LNode(None)
    cur = head
    i = 1
    print 'LinkedList: ',
    while i <= l:
        n = random.randint(0,9)
        tmp = LNode(n)
        print tmp.data,
        cur.next = tmp
        cur = tmp
        i += 1
    return head

def rotateK(head, k):
    print '\n k: ',k,
    i = 1
    slow = head.next
    fast = head.next
    while i <= k:
        if fast.next is not None:
            fast = fast.next
        else:
            print '\nout of range'
            return
        i += 1
    while fast.next is not None:
        slow = slow.next
        fast = fast.next
    tmp1 = slow.next
    slow.next = None
    tmp2 = head.next
    head.next = tmp1
    fast.next = tmp2
    return head

def printLinkedList(head):
    cur = head.next
    print "\nafter rotate: ",
    while cur is not None:
        print cur.data,
        cur = cur.next


if __name__ == '__main__':
    head = createLinkedList(10)
    rotateK(head, 3)
    printLinkedList(head)

