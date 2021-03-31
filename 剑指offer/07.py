# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# 返回如下的二叉树：
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 前序遍历性质： 节点按照 [ 根节点 | 左子树 | 右子树 ] 排序。
# 中序遍历性质： 节点按照 [ 左子树 | 根节点 | 右子树 ] 排序。
# 前序遍历的第一个节点就是根。在中序遍历中通过根 区分左子树和右子树。
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        def recur(root, left, right):
            if left > right: return                               # 递归终止
            node = TreeNode(preorder[root])                       # 建立根节点
            i = dic[preorder[root]]                               # 划分根节点、左子树、右子树
            node.left = recur(root + 1, left, i - 1)              # 开启左子树递归
            node.right = recur(i - left + root + 1, i + 1, right) # 开启右子树递归
            return node                                           # 回溯返回根节点

        dic, preorder = {}, preorder
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        # {9: 0, 3: 1, 15: 2, 20: 3, 7: 4}
        return recur(0, 0, len(inorder) - 1)
        # 0, 0, 4
        # 1, 0, 0 left root+1, left=0, 1-1
        # 2, 2, 4 right 1-0+0+1, i+1, 4
        # 3, 2, 2 left
        # 4, 4, 4 right

if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    s = Solution()
    s.buildTree(preorder, inorder)