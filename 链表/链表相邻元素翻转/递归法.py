# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 递归三要素
# 1.退出条件，不足两个元素
# 2.下级递归的传入，返回值，传入需要交换的部分，返回已经交换好的部分。
# 3.本级递归的作用，对 head next 和 已经交换好的部分，交换 head 和 next的位置。
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
        # print tmp.data,
        cur.next = tmp
        cur =tmp
        i += 1
    return head

def printLinkedList(head):
    while head is not None:
        print head.data,
        head = head.next

def switch(head):
    if head is None or head.next is None:
        return head
    newHead = head.next
    head.next = switch(newHead.next)
    newHead.next = head
    return newHead

if __name__ == '__main__':
    head = createLinkedList(8)
    # 去掉 None,1
    head = head.next
    printLinkedList(head)
    head = switch(head)
    print '\n'
    printLinkedList(head)

