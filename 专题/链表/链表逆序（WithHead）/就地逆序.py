# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 就地逆序
class LNode:
    def __new__(self,x):
        self.data=x
        self.next=None

# 关注x.next，这才是移动指针

# 方法功能: 对单链表进行逆序 输入参数：head 链表头结点
def Reverse(head):
    # 判断链表是否为空
    if head==None or head.next==None or head.next.next==None:
        return
    pre=None # 前一个节点
    cur=None # 当前节点
    next=None # 下个节点
    # 把链表首节点变为尾结点
    cur=head.next # 1,->2
    next=cur.next # 2,->3
    cur.next=None # 1,->2;1,->None 头变尾
    pre=cur # pre: 1,None
    cur=next # cur: 2,->3
    # 使当前遍历到的结点cur 指向前一个结点？
    while cur.next!=None:
        next=cur.next # 2,->3;3,->4
        cur.next=pre # 2,->1;3,->2;4,->3;5,->4;6,->5; cur 指向前一个！
        pre=cur # 2,->1;3,->2
        cur=cur.next # 1,None;2,->1
        cur=next # 2,->3;3,->4
    # 链表最后一个结点指向倒数第二个结点 7->6
    cur.next=pre
    # 链表的头结点指向原来链表的尾结点? head->7
    head.next=cur

if __name__=="__main__":
    i=1
    # 链表头结点？
    head=LNode()
    head.next=None
    tmp=None
    cur=head
    # head 不存在，None
    # cur 不存在，None
    # 构造单链表
    # 即构造 cur 的下一个是 tmp
    while i<8:
        tmp=LNode()
        tmp.data=i # 1;2
        tmp.next=None # 1,None;2,None
        if i == 1:
            print "cur","nil",cur.next
            # cur: nil,None
        if i == 2:
            print "cur",cur.data,cur.next
            # cur: 1,None
        if i == 1:
            print "head.next before1", head.next
        if i == 2:
            print "head.next before2",head.next,head.next.next
        cur.next=tmp # 不存在,->1;1,->2
        if i == 1:
            print "head.next after1", head.next
        if i == 2:
            print "haed.next after2",head.next,head.next.next
        cur=tmp # 1,None;2,None
        i+=1
    print "逆序前： ",
    # print "head:",head,"head.next",head.next,"head.next.next",head.next.next
    # ->head,->1,->2
    # print "cur:",cur.data,cur.next # 7 None
    cur=head.next # 从第一个元素开始
    while cur!=None:
        print  cur.data,
        cur=cur.next
    print "\n逆序后：",
    Reverse(head)
    cur=head.next # 从第一个元素开始
    while cur!=None:
        print cur.data,
        cur=cur.next
