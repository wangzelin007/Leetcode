# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 中序遍历
class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def getK(k):
            if k <= len(self.arr):
                return self.arr[-k]

        def dfs(root):
            if not root: return
            dfs(root.left)
            self.arr.append(root.val)
            dfs(root.right)

        self.arr = []
        dfs(root)
        return getK(k)

# 中序遍历的倒序
class Solution(object):
    def kthLargest(self, root, k):
        def dfs(root):
            if not root: return
            dfs(root.right)
            if self.k == 0: return
            self.k -= 1
            if self.k == 0: self.res = root.val
            dfs(root.left)

        self.k = k
        dfs(root)
        return self.res