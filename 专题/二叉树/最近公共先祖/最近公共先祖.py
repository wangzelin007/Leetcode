# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# offer 68 && leetcode 236/235
# root 左侧包含 p or q && root 右侧包含p or q return root
# root 左侧不包含p or q && root 右侧不包含p or q return
# root 左侧包含p or q && root 右侧不包含 p or q return left
# root 左侧不包含 p or q && root 右侧包含 p or q return right

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 二叉树解法
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == q or root == p: return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if not left: return right
        if not right: return left
        return root

# 二叉搜索树解法
# 二叉搜索树：
# 左子树的所有节点都小于当前节点，右子树的所有节点都大于当前节点，并且每棵子树都具有上述特点
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        while (root.val-p.val)*(root.val-q.val) > 0: root=(root.lefg,root.right)[p.val>root.val]
        return root
# [True] == [1] ; [False] == [0]

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        return root

