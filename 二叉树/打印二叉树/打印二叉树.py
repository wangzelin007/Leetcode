# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# O(N) && O(N)
# 每个结点都访问了一次
# 使用list 存储了结点
from collections import deque

class BiTNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

def arrayToTree(arr,start,end):
    # root = None
    if end >= start:
        root = BiTNode()
        mid = (start+end+1)/2
        root.data = arr[mid]
        root.lchild = arrayToTree(arr,start,mid-1)
        root.rchild = arrayToTree(arr,mid+1,end)
    else:
        root = None
    return root

def printTreeLayer(root):
    if root == None:
        return
    q = deque()
    q.append(root)
    while len(q) > 0:
        tmp = q.popleft()
        print(tmp.data),
        if tmp.lchild:
            q.append(tmp.lchild)
        if tmp.rchild:
            q.append(tmp.rchild)

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9,10]
    root = arrayToTree(arr,0,len(arr)-1)
    printTreeLayer(root)