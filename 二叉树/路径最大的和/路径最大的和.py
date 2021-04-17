# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None

class InitRef:
    def __init__(self):
        self.max = None

def Max(a,b,c):
    max = a if a>b else b
    max = max if max>c else c
    return max

def findMaxPathRecur(root,m):
    if not root:
        return 0
    else:
        Left = findMaxPathRecur(root.lchild,m)
        Right = findMaxPathRecur(root.rchild,m)
        maxAll = Left+Right+root.data
        maxLeft = Left+root.data
        maxRight = Right+root.data
        tmpMax = Max(maxLeft,maxRight,maxAll)
        if tmpMax > m.max:
            m.max = tmpMax
        sumMax = Left if Left > Right else Right
        return sumMax+root.data

if __name__ == '__main__':
    root = TreeNode(2)
    left = TreeNode(3)
    right = TreeNode(5)
    root.lchild = left
    root.rchild = right
    m = InitRef()
    m.max = -2**31
    findMaxPathRecur(root,m)
    print(m.max,end=" ")