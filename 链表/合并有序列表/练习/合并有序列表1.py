# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
class LNode(object):
    def __init__(self,x):
        self.data = x
        self.next = None

def createLinkedList(l):
    head1 = LNode(None)
    head2 = LNode(None)
    i1 = 1
    i2 = 2
    cur1 = head1
    cur2 = head2
    while i1 / 2 <= l:
        tmp1 = LNode(i1+2)
        tmp2 = LNode(i2+2)
        cur1.next = tmp1
        cur2.next = tmp2
        cur1 = tmp1
        cur2 = tmp2
        i1 += 2
        i2 += 2
    return head1,head2

def printLinkedList(head):
    if head.data:
        cur = head
    else:
        cur = head.next
    while cur:
        print cur.data,
        cur = cur.next

def merge(head1, head2):
    if not head1 or not head1.next:
        return head2
    if not head2 or not head2.next:
        return head1
    cur1 = head1.next
    cur2 = head2.next
    head = LNode(None)
    cur = head
    while cur1 and cur2:
        if cur1.data < cur2.data:
            cur.next = cur1
            cur = cur1
            cur1 = cur1.next
        else:
            cur.next = cur2
            cur = cur2
            cur2 = cur2.next
    if cur1:
        cur.next = cur1
    if cur2:
        cur.next = cur2
    return head

if __name__ == '__main__':
    head1, head2 = createLinkedList(10)
    printLinkedList(head1)
    print '\n'
    printLinkedList(head2)
    head = merge(head1, head2)
    print '\n'
    printLinkedList(head)
