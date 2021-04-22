# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
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

def reverseLinkedList(head):
    """
    # 递归法
    # 1.退出条件 head is None or head.next is None ;return head
    # 2.递归入参 head.next; 递归返回 newHead
    # 3.指向前一个结点
    """
    if head is None or head.next is None:
        return head
    newHead = reverseLinkedList(head.next)
    head.next.next = head
    head.next = None
    return newHead

def reverse(head):
    if head is None:
        return
    first = head.next
    newFirst = reverseLinkedList(first)
    head.next = newFirst

if __name__ == '__main__':
    head = createLinkedList(8)
    printLinkedList(head)
    reverse(head)
    print '\n'
    printLinkedList(head)