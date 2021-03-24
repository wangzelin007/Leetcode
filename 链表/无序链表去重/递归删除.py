# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
    O(N^2) && 很多空间
"""
class LNode:
    def __new__(self,x):
        LNode.data = x
        LNode.next = None

def remove(head):
    if head is None:
        return
    head.next = removeDupRecursion(head.next)

def removeDupRecursion(head):
    if head.next is None:
        return head
    pointer = None
    cur = head
    head.next = removeDupRecursion(head.next)
    pointer = head.next
    while pointer is not None:
        if head.data == pointer.data:
            cur.next = pointer.next
            pointer = cur.next
        else:
            pointer = pointer.next
            cur = cur.next
    # head cur pointer 三个变量，每次都要修改cur和pointer的位置
    return head

if __name__ == '__main__':
    head = LNode()
    head.next = None
    cur = head
    i = 1
    while i < 12:
        tmp = LNode()
        tmp.next = None
        if i % 2 == 0:
            tmp.data = i+1
        elif i % 3 == 0:
            tmp.data = i-2
        else:
            tmp.data = i
        cur.next = tmp
        cur = tmp
        i += 1
    print "去重前：",
    cur = head.next
    while cur is not None:
        print cur.data,
        cur = cur.next
    remove(head)
    print "去重后：",
    cur = head.next
    while cur is not None:
        print cur.data,
        cur = cur.next