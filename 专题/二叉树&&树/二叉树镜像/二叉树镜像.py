# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# offer 27 leetcode 226
# 递归
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return
        left = self.mirrorTree(root.right)
        right = self.mirrorTree(root.left)
        root.left = left
        root.right = right
        return root

# 栈
class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left: stack.append(root.left)
            if node.right: stack.append(root.right)
            node.left,node.right = node.right,node.left
        return root
