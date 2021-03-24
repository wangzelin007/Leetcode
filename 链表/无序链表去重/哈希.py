# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
import random

def RemoveDup(head):
    if head.next is None:
        return head
    hashSet = set()
    hashSet.clear()
    pre = head
    cur = head.next
    while cur is not None:
        if cur.data in hashSet:
            pre.next = cur.next
        else:
            hashSet.add(cur.data)
            pre = pre.next
        cur = cur.next
    return head

class LNode(object):
    def __init__(self,x):
        self.data = x
        self.next = None

if __name__ == '__main__':
    head = LNode(None)
    cur = head
    i = 1
    while i < 12:
        n = random.randint(0,9)
        tmp = LNode(n)
        cur.next = tmp
        cur = tmp
        i += 1
    print "before:",
    cur = head.next
    while cur is not None:
        print cur.data,
        cur = cur.next
    RemoveDup(head)
    print "\nafter",
    cur = head.next
    while cur is not None:
        print cur.data,
        cur = cur.next


