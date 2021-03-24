# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# O(N) && 0(N)
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
    cur.next = head.next.next.next
    return head

def printLinkedList(head):
    cur = head.next
    i = 1
    while i <= 8:
        print cur.data,cur.next
        cur = cur.next
        i += 1

def isLoop(head):
    hashList = []
    cur = head.next
    i = 1
    while True:
        if not cur:
            print 'no Loop'
            return False
        elif cur.next not in hashList:
            hashList.append(cur.next)
            cur = cur.next
            i += 1
        else:
            print hashList
            x = hashList.index(cur.next) + 1
            print 'is Loop',cur.data,cur.next,'入口',x
            return True

if __name__ == '__main__':
    head = createLinkedList(8)
    printLinkedList(head)
    isLoop(head)
