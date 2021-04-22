# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# O(N)
class BiTNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

class Test:
    def __init__(self):
        self.maxSum = -2**31 #给一个足够小的值

    def findMaxSubTree(self,root,maxRoot):
        if root == None:
            return 0
        lmax = self.findMaxSubTree(root.lchild,maxRoot)
        rmax = self.findMaxSubTree(root.rchild,maxRoot)
        sums = lmax+rmax+root.data
        if sums > self.maxSum:
            self.maxSum = sums
            maxRoot.data = root.data
        return sums

    def constructTree(self):
        root = BiTNode()
        node1 = BiTNode()
        node2 = BiTNode()
        node3 = BiTNode()
        node4 = BiTNode()
        root.data = 6
        node1.data = 3
        node2.data = -7
        node3.data = -1
        node4.data = 9
        root.lchild = node1
        root.rchild = node2
        node1.lchild = node3
        node1.rchild = node4
        print(node2.lchild,node2.rchild,node3.lchild,node3.rchild,node4.lchild,node4.rchild)
        return root


if __name__ == '__main__':
    test = Test()
    root = test.constructTree()
    maxRoot = BiTNode()
    test.findMaxSubTree(root,maxRoot)
    print('最大子树和：' + str(test.maxSum))
    print('对应的根结点：' + str(maxRoot.data))