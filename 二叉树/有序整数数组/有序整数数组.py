# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
class BiTNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

def arrayToTree(arr,start,end):
    root = None
    if end >= start:
        root = BiTNode()
        mid = (start+end+1)//2 # mid 是下标
        root.data = arr[mid]
        # start end 看似不变，其实可能会变为mid+1和mid-1
        root.lchild = arrayToTree(arr, start, mid-1)
        root.rchild =  arrayToTree(arr, mid+1, end)
    else:
        root = None
    return root

def printTreeMidOrder(root):
    # 中序递归遍历 左中右
    if root == None:
        return
    if root.lchild:
        printTreeMidOrder(root.lchild)
    print(root.data, end=" ")
    if root.rchild:
        printTreeMidOrder(root.rchild)

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9,10]
    print("数组：", end=" ")
    i=0
    while i<len(arr):
        print(arr[i], end=" ")
        i += 1
    root = arrayToTree(arr,0,len(arr)-1)
    print("\n数的中序遍历：",end=" ")
    printTreeMidOrder(root)
