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
    if end >= start:
        root = BiTNode()
        mid = (start+end+1)//2
        root.data = arr[mid]
        root.lchild = arrayToTree(arr,start,mid-1)
        root.rchild = arrayToTree(arr,mid+1,end)
    else:
        root = None
    return root

def printTree(root):
    # 左 中 右
    if root == None:
        return
    if root.lchild:
        printTree(root.lchild)
    print(root.data,end=" ")
    if root.rchild:
        printTree(root.rchild)

def printLayerTree(root):
    # 逐层打印
    if root == None:
        return
    q = deque()
    q.append(root)
    while len(q) > 0:
        tmp = q.popleft()
        print(tmp.data,end=" ")
        if tmp.lchild:
            q.append(tmp.lchild)
        if tmp.rchild:
            q.append(tmp.rchild)

def isEqual(root1,root2):
    if root1 == root2 == None:
        return True
    if root1 == None and root2 != None:
        return False
    if root1 != None and root2 == None:
        return False
    if root1.data == root2.data:
        return isEqual(root1.lchild,root2.lchild) and isEqual(root1.rchild,root2.rchild)
    else:
        return False

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9,10]
    long = len(arr)
    root = arrayToTree(arr,0,long-1)
    printTree(root)
    print('\n')
    printLayerTree(root)
    print(isEqual(root,root))
    arr2 = [1,2,3,4,5,6,7,8,9,11]
    long2 = len(arr2)
    root2 = arrayToTree(arr2,0,long2-1)
    printTree(root2)
    print(isEqual(root,root2))