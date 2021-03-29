# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
from collections import deque

class BiTNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

def arrayToTree(arr,start,end):
    root = None
    if end >= start:
        mid = (start+end+1)/2
        root = BiTNode()
        root.data = arr[mid]
        root.lchild = arrayToTree(arr,start,mid-1)
        root.rchild = arrayToTree(arr,mid+1,end)
    else:
        root = None
    return root

def printForwardTree(root):
    # 前序遍历 中左右
    if not root:
        return
    print root.data,
    if root.lchild:
        printForwardTree(root.lchild)
    if root.rchild:
        printForwardTree(root.rchild)

def printTree(root):
    # 中序遍历 左中右
    if not root:
        return
    if root.lchild:
        printTree(root.lchild)
    print root.data,
    if root.rchild:
        printTree(root.rchild)

def printBackTree(root):
    # 后序 左右中
    if not root:
        return
    if root.lchild:
        printBackTree(root.lchild)
    if root.rchild:
        printBackTree(root.rchild)
    print root.data,

def printLayerTree(root):
    if not root:
        return
    q = deque()
    q.append(root)
    while len(q) > 0:
        root = q.popleft()
        print root.data,
        if root.lchild:
            q.append(root.lchild)
        if root.rchild:
            q.append(root.rchild)

def copyTree(root):
    if not root:
        return
    copyRoot = BiTNode()
    copyRoot.data = root.data
    if root.lchild:
        copyRoot.lchild = copyTree(root.lchild)
    if root.rchild:
        copyRoot.rchild = copyTree(root.rchild)
    return copyRoot

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9,10]
    root = arrayToTree(arr,0,len(arr)-1)
    printForwardTree(root)
    print '\n'
    printTree(root)
    print '\n'
    printLayerTree(root)
    print '\n'
    printBackTree(root)
    root1 = copyTree(root)
    print '\n'
    printTree(root1)
    print '\n'
    printLayerTree(root1)
    print '\n'
    printBackTree(root1)
