# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：
#
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
# 即奇数层正序打印，偶数层倒序打印

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res,q = [],deque()
        q.append(root)
        while q:
            tmp = deque()
            for _ in range(len(q)):
                node = q.popleft()
                if len(res) % 2: tmp.appendleft(node.val)
                else: tmp.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(list(tmp))
        return res