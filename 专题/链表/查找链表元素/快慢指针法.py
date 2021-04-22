# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# O(N) && O(1)
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
    if head is None or head.next is None:
        return head
    i = 1
    curs = head.next
    curf = head.next
    while i <= k:
        if curf.next is None:
            print "\n out of range"
            return
        else:
            curf = curf.next
        i += 1
    while curf is not None:
        curs = curs.next
        curf = curf.next
    print "\nk: ",k,"value: ",curs.data


if __name__ == '__main__':
    head = createLinkedList(11)
    searchLinkedList(5, head)