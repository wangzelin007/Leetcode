# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 二叉排序树

class BiTNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

def getMaxNode(root):
    if not root: return
    while root.rchild:
        root = root.rchild
    return root

def getMinNode(root):
    if not root: return
    while root.lchild:
        root = root.lchild
    return root

def arrayToTree(arr,start,end):
    if end >= start:
        root = BiTNode()
        mid = (start+end+1)/2
        root.data = arr[mid]
        root.lchild = arrayToTree(arr,start,mid-1)
        root.rchild = arrayToTree(arr,mid+1,end)
    else:
        root = None
    return root

def printTree(root):
    if not root: return
    printTree(root.lchild)
    print root.data,
    printTree(root.rchild)

def finNode(root):
    min = getMinNode(root)
    max = getMaxNode(root)
    mid = (min.data+max.data)/2
    # print mid
    result = None
    while root:
        if root.data <= mid:
            root = root.rchild
        else:
            result = root.data
            root = root.lchild
    return result

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7]
    root = arrayToTree(arr,0,len(arr)-1)
    printTree(root)
    print '\n'
    print(finNode(root))

