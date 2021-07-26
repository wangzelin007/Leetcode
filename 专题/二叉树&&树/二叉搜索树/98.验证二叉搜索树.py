# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
# 假设一个二叉搜索树具有如下特征：
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 二叉搜索树 inorder 为有序列表，将有序列表和直接去重排序的结果比较。
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        inorder = self.inorder(root)
        return inorder == list(sorted(set(inorder)))

    def inorder(self, root):
        if not root: return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

# 2. 在inorder递归的过程中，比较前一个结点和当前节点的大小。
# 注意 self.pre = root
class Solution(object):
    def isValidBST(self, root):
        self.pre = None
        return self.helper(root)

    def helper(self, root):
        if not root:
            return True
        if not self.helper(root.left):
            return False
        if self.pre and self.pre.val >= self.root.val:
            return False
        self.pre = root
        return self.helper(root.right)

