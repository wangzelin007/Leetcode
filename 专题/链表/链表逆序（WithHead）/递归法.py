# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 递归法
"""
链表struct
"""
class LNode:
    def __new__(self,x):
        self.data=x
        self.next=None

"""
对不带头结点的单链表进行逆序
输入参数：链表第一个结点
"""
def RecursiveRevers(first):
    # 如果链表为空或者只有一个元素，直接返回
    if first is None or first.next is None:
        print first.data,
        return first
    # 反转后面的结点
    newFirst=RecursiveRevers(first.next)
    # 把当前结点加到逆序后链表的尾部
    first.next.next=first
    first.next=None
    print first.data,
    return newFirst

"""
对带头结点的单链表进行逆序
输入参数：head 链表头结点
"""
def Reverse(head):
    if head is None:
        return
    # 获取第一个结点
    firstNode=head.next
    # 逆序
    newFirst=RecursiveRevers(firstNode)
    # 头结点指向逆序后的第一个结点
    head.next=newFirst
    return newFirst

if __name__ == '__main__':
    # head
    head=LNode()
    head.next=None
    tmp=None
    cur=head
    i=1
    while i < 8:
        tmp=LNode()
        tmp.data=i
        tmp.next=None
        cur.next=tmp
        cur=tmp
        i += 1
    print "逆序前：",
    cur=head.next
    while cur!=None:
        print cur.data,
        cur=cur.next
    print "\n逆序后：",
    Reverse(head)
    cur=head.next
    while cur!=None:
        print cur.data,
        cur=cur.next