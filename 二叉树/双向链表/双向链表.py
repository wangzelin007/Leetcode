# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# leetcode 426 Offer 36
class BiTNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

class Test:
    def __init__(self):
        self.pHead = None
        self.pEnd = None

    def arrayToTree(self,arr,start,end):
        root = None
        if end >= start:
            mid = (start+end+1)/2
            root = BiTNode()
            root.data = arr[mid]
            root.lchild = self.arrayToTree(arr,start,mid-1)
            root.rchild = self.arrayToTree(arr,mid+1,end)
        else:
            root = None
        return root

    def inOrderBSTree(self,root):
        if root == None:
            return
        self.inOrderBSTree(root.lchild)
        # self.pEnd is pre;root is cur;self.pHead is stable
        if self.pEnd == None:
            self.pHead = root
        else:
            # self.pEnd.lchild = root
            self.pEnd.rchild,root.lchild = root,self.pEnd
        self.pEnd = root
        self.inOrderBSTree(root.rchild)

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9,10]
    test = Test()
    root = test.arrayToTree(arr,0,len(arr)-1)
    test.inOrderBSTree(root)
    cur = test.pHead
    while cur:
        print cur.data,
        cur = cur.rchild
    print '\n'
    cur = test.pEnd
    while cur:
        print cur.data,
        cur = cur.lchild
