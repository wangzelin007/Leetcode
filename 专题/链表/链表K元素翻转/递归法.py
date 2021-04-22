# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 1. 退出条件，少于k个元素
# 2. 下级递归的传入和返回，传入k个元素，对其逆序
# 3. 本级递归的作用，把翻转链和已翻转链以及未翻转链连接起来。
# head>1>2>3>4>5>6>7>8>9>10
import random

class LNode(object):
    def __init__(self,x):
        self.data = x
        self.next = None

def createLinkedList(l):
    head = LNode(1)
    cur = head
    i = 1
    while i <= l-1:
        n = random.randint(0,9)
        tmp = LNode(n)
        cur.next = tmp
        cur = tmp
        i += 1
    return head

def printLinkedList(head):
    cur = head
    while cur is not None:
        print cur.data,cur
        cur = cur.next

def reverseKGroup(head, k):
    cur = head
    count = 0
    # cur 前移k
    while cur and count!= k:
        cur = cur.next
        count += 1
    if count == k:
        cur = reverseKGroup(cur, k)
        while count:
            tmp = head.next
            head.next = cur
            cur = head
            head = tmp
            count -= 1
        head = cur
    return head

if __name__ == '__main__':
    head = createLinkedList(10)
    printLinkedList(head)
    head = reverseKGroup(head, 3)
    print '\n'
    printLinkedList(head)