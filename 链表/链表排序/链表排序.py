# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 1.将链表一分为二 FindMiddleNode
# 2.将后半部分逆序 Reverse
# 3.将两个链表依次合并 Reorder
import random

class LNode(object):
    def __init__(self,x):
        self.data = x
        self.next = None

def createLinkedList(l):
    head = LNode(None)
    i = 1
    cur = head
    while i <= l:
        n = random.randint(0,9)
        tmp = LNode(n)
        cur.next = tmp
        cur = tmp
        i += 1
    return head

def FindMiddleNode(head):
    # 0个或1个
    if head is None or head.next is None:
        return head
    fast = head
    slow = head
    preSlow = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        preSlow = slow
        slow = slow.next
    preSlow.next = None
    return slow

def Reverse(first):
    if first.next:
        newFirst = RecursiveReverse(first)
    return newFirst

def RecursiveReverse(first):
    if first is None or first.next is None:
        return first
    else:
        newFirst = RecursiveReverse(first.next)
        first.next.next = first
        first.next = None
    return newFirst

def Reorder(head):
    # head is None or 1 is None or 2 is None
    if head is None or head.next is None or head.next.next is None:
        return
    cur1 = head.next
    mid = FindMiddleNode(head.next)
    # print "\ncur1",cur1.data,cur1.next.data,cur1.next.next.data,cur1.next.next.next.data,
    print "\nmid",mid.data
    cur2 = Reverse(mid)
    # print "cur2",cur2.data,cur2.next.data,cur2.next.next.data,cur2.next.next.next.data,cur2.next.next.next.next.data,
    # 总结一下 只改next；1，2往后移动一位
    # cur1.next = cur2
    # cur1 = cur1.next *** 使用tmp
    # cur2.next = cur1
    # cur2 = cur2.next *** 使用tmp
    while cur1.next is not None:
        print "\ncur1.data",cur1.data
        tmp = cur1.next
        cur1.next = cur2
        cur1 = tmp
        tmp = cur2.next
        cur2.next = cur1
        cur2 = tmp
    print "\ncur1.next",cur1.next
    cur1.next = cur2 # mid


if __name__ == '__main__':
    LinkedList = createLinkedList(10)
    cur = LinkedList.next
    print "排序前："
    while cur is not None:
        print cur.data,
        cur = cur.next
    Reorder(LinkedList)
    cur = LinkedList.next
    print "\n排序后："
    while cur is not None:
        print cur.data,
        cur = cur.next
