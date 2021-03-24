# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# O(N) && O(N)
import random

class LNode(object):
    def __init__(self, x):
        self.data = x
        self.next = None

def createLinkedList(l):
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

def add(head1, head2):
    cur1 = head1.next
    cur2 = head2.next
    c = 0
    head = LNode(None)
    cur = head
    while cur1 is not None and cur2 is not None:
        sum = cur1.data + cur2.data + c
        x = sum % 10
        tmp = LNode(x)
        cur.next = tmp
        c = sum / 10
        cur1 = cur1.next
        cur2 = cur2.next
        cur = tmp
    while cur1 is None and cur2 is not None:
        sum = cur2.data + c
        x = sum % 10
        tmp = LNode(x)
        cur.next = tmp
        c = sum / 10
        cur2 = cur2.next
        cur = tmp
    while cur1 is not None and cur2 is None:
        sum = cur1.data + c
        x = sum % 10
        tmp = LNode(x)
        cur.next = tmp
        c = sum / 10
        cur1 = cur1.next
        cur = tmp
    # 进位符号c
    if c:
        tmp = LNode(c)
        cur.next = tmp
    return head


if __name__ == '__main__':
    l1 = random.randint(0,10)
    l2 = random.randint(0,10)
    LinkedList1 = createLinkedList(l1)
    LinkedList2 = createLinkedList(l2)
    print("add: \n"),
    cur = LinkedList1.next
    while cur is not None:
        print cur.data,
        cur = cur.next
    print '\n'
    cur = LinkedList2.next
    while cur is not None:
        print cur.data,
        cur = cur.next
    head = add(LinkedList1,LinkedList2)
    cur = head.next
    print("\nresult:"),
    while cur is not None:
        print cur.data,
        cur = cur.next