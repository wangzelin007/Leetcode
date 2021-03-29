# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# O(N) && O(1)
# level = int(math.log(10,2))+1
import math

class BiTNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

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

def printAtLevel(root,level):
    if root == None or level < 0:
        return 0
    elif level == 0:
        print root.data,
        return 1
    else:
        return printAtLevel(root.lchild,level-1)+printAtLevel(root.rchild,level-1)

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9,10]
    long = len(arr)
    level = int(math.log(long,2))+1
    root = arrayToTree(arr,0,long-1)
    printAtLevel(root,level)
    i = 0
    while i < level:
        printAtLevel(root,i)
        i += 1
