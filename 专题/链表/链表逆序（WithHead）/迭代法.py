# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# head->1->2->3->4->5->None
# 1->2->3->4->5->None
# None<-1 2->3->4->5
# None<-1<-2 3->4->5
# None<-1<-2<-3 4->5
# None<-1<-2<-3<-4 5
# None<-1<-2<-3<-4<-5
# None<-1<-2<-3<-4<-5<-head
import random


def reverse(head):
    if head is None or head.next is None:
        return
    pre = None
    cur = head.next
    # next = None
    while cur is not None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    return pre

# good
def reverseNohead(head):
    if head is None or head.next is None:
        return
    pre = None
    cur = head
    next = None
    while cur is not None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    return pre

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

def createLinkedListNohead(l):
    head = LNode(1)
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
    while cur is not None:
        print cur.data,
        cur = cur.next

if __name__ == '__main__':
    head = createLinkedList(8)
    printLinkedList(head)
    print '\n'
    head = reverse(head)
    printLinkedList(head)
    print '\n'
    head = createLinkedListNohead(8)
    printLinkedList(head)
    print '\n'
    head = reverseNohead(head)
    printLinkedList(head)

