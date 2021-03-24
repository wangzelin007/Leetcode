# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# O(N^2)
import random

class LNode(object):
    def __init__(self,x):
        self.data = x
        self.next = None

def createLinkedList(l):
    head = LNode(None)
    cur = head
    i = 1
    print "LinkedList: ",
    while i <= l:
        n = random.randint(0,9)
        tmp = LNode(n)
        print tmp.data,
        cur.next = tmp
        cur = tmp
        i += 1
    return head

def searchLinkedList(k, head):
    len = 0
    i = 0
    cur = head
    while cur.next is not None:
        len += 1
        cur = cur.next
    print "\nlen: ",len
    cur = head
    while i <= (len-k):
        cur = cur.next
        i += 1
    print "\nk: ",k,"value: ",cur.data

if __name__ == '__main__':
    head = createLinkedList(11)
    searchLinkedList(3, head)