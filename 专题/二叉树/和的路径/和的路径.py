# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 前序遍历
# 示例:
# 给定如下二叉树，以及目标和 target = 22，
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# 返回:
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: List[List[int]]
        """
        res,path=[],[]
        def recur(root, target):
            if not root: return
            path.append(root.val)
            target -= root.val
            if target == 0 and root.left == None and root.right == None:
                # 太精髓了，这里如果没有list 是浅拷贝，导致res一直变化。不是正确答案！
                res.append(list(path))
            recur(root.left,target)
            recur(root.right,target)
            path.pop()
        recur(root,target)
        return res