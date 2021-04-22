# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 双链表排序的递归版本
# 多层递归
class LNode(object):
    def __init__(self,x):
        self.data = x
        self.right = None
        self.down = None

def createLinkedList():
    head = LNode(None)
    cur = head
    cur.right = LNode(3)
    cur = cur.right
    cur.down = LNode(6)
    cur.down.down = LNode(8)
    cur.down.down.down = LNode(31)
    cur.right = LNode(11)
    cur = cur.right
    cur.down = LNode(21)
    cur.right = LNode(15)
    cur = cur.right
    cur.down = LNode(22)
    cur.down.down = LNode(50)
    cur.right = LNode(30)
    cur = cur.right
    cur.down = LNode(39)
    cur.down.down = LNode(40)
    cur.down.down.down = LNode(55)
    return head

def printLinkedList(head):
    if head.data:
        cur = head
    else:
        cur = head.down
    while cur:
        print cur.data,
        cur = cur.down
    print '\n'

def printLinkedListAll(head):
    if head.data:
        cur = head
    else:
        cur = head.right
    while cur:
        first = cur
        print cur.data,
        while cur.down:
            cur = cur.down
            print cur.data,
        cur = first.right
    print '\n'

def recursiveMergeOuter(head):
    if head is None or head.right is None:
        return head
    head.right = recursiveMergeOuter(head.right)
    head = recursiveMergeInner(head, head.right)
    return head

def recursiveMergeInner(a, b):
    if a is None:
        return b
    if b is None:
        return a
    if a.data < b.data:
        result = a
        result.down = recursiveMergeInner(a.down, b)
    else:
        result = b
        result.down = recursiveMergeInner(a, b.down)
    return result

if __name__ == '__main__':
    head = createLinkedList()
    printLinkedListAll(head)
    head = recursiveMergeOuter(head.right)
    # head = recursiveMergeOuter(head)
    printLinkedList(head)
