# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
def Revers(head):
    if head is None or head.next is None:
        return
    cur=None
    next=None
    cur=head.next.next
    # 设置原链表的第一个结点为尾结点！
    head.next.next=None
    # 遍历修改 head.next && cur.next
    while cur is not None:
        next=cur.next
        cur.next=head.next
        head.next=cur
        cur=next
    return head

class LNode:
    def __new__(self,x):
        self.data=x
        self.next=None

if __name__ == '__main__':
    # head
    i=1
    head=LNode()
    head.next=None
    tmp=None
    cur=head
    while i < 8:
        tmp=LNode()
        tmp.data=i
        tmp.next=None
        cur.next=tmp
        cur=tmp
        i += 1
    print "逆序前：",
    cur=head.next
    while cur is not None:
        print cur.data,
        cur=cur.next
    Revers(head)
    cur=head.next
    print "\n逆序后：",
    while cur is not None:
        print cur.data,
        cur=cur.next
