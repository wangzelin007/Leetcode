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
    

def printTreeMidOrder(root):
    # 中序递归遍历
    pass

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9,10]
    print "数组：",
    i=0
    while i<len(arr):
        print arr[i],
        i += 1
    root = arrayToTree(arr,0,len(arr)-1)
    print "\n数的中序遍历：",
    printTreeMidOrder(root)
