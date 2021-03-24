# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
    O(N^2) && O(1)
"""

class LNode:
    def __new__(self,x):
        LNode.data=x
        LNode.next=None

def removeDup(head):
    if head is None or head.next is None:
        return
    innerCur = None
    innerPre = None
    outerCur = head.next
    while outerCur is not None:
        innerCur = outerCur.next
        innerPre = outerCur
        while innerCur is not None:
            if outerCur.data == innerCur.data:
                innerPre.next = innerCur.next
            else:
                innerPre = innerCur
            innerCur = innerCur.next
        outerCur = outerCur.next

if __name__ == '__main__':
    head=LNode()
    head.next=None
    cur = head
    i = 1
    while i < 12:
        tmp=LNode()
        if i % 2 == 0:
            tmp.data = i+1
        elif i % 3 == 0:
            tmp.data = i-2
        else:
            tmp.data = i
        tmp.next = None # 容易漏
        cur.next = tmp
        cur = tmp
        i += 1
    print "删除前：",
    cur = head.next
    while cur is not None:
        print cur.data,
        cur = cur.next
    print "删除后：",
    removeDup(head)
    cur = head.next
    while cur is not None:
        print cur.data,
        cur = cur.next