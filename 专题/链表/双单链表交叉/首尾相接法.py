# 无环链表是否相交
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
    head1 = LNode(None)
    head2 = LNode(None)
    cur1 = head1
    cur2 = head2
    cur1.next = LNode(1)
    cur2.next = LNode(2)
    cur1 = cur1.next
    cur2 = cur2.next
    i = 1
    while i < l:
        n = random.randint(0,9)
        tmp = LNode(n)
        cur1.next = tmp
        cur2.next = tmp
        cur1 = tmp
        cur2 = tmp
        i += 1
    return head1, head2

def createLinkedList2(l):
    head = LNode(None)
    cur = head
    i = 1
    while i < l:
        n = random.randint(0,9)
        tmp = LNode(n)
        cur.next = tmp
        cur = tmp
        i += 1
    return head

def printLinkedList(head):
    if head.data is None:
        cur = head.next
    else:
        cur = head
    while cur:
        print cur.data,
        cur = cur.next

def cross(head1, head2):
    cur1 = head1.next
    cur2 = head2.next
    while cur1.next:
        cur1 = cur1.next
    cur1.next = cur2
    fast = head1.next
    slow = head1.next
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return slow
    return False


if __name__ == '__main__':
    head1, head2 = createLinkedList(8)
    printLinkedList(head1)
    print '\n'
    printLinkedList(head2)
    print(cross(head1, head2))
    head3 = createLinkedList2(8)
    head4 = createLinkedList2(8)
    printLinkedList(head3)
    print '\n'
    printLinkedList(head4)
    print(cross(head3, head4))

