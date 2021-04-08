# 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，
# 第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
#
# 例如:
# 给定二叉树:[3,9,20,null,null,15,7],
#
#       3
#      / \
#     9  20
#        / \
#       15  7
# 返回其层次遍历结果：
# [
#     [3],
#     [20,9],
#     [15,7]
# ]
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        stack, res, layer = deque(), [], 1
        stack.append(root)
        while stack:
            tmp = []
            for _ in range(len(stack)):
                root = stack.popleft()
                tmp.append(root.val)
                if root.left: stack.append(root.left)
                if root.right: stack.append(root.right)
            stack.append(tmp if layer % 2 else tmp[::-1])
            layer += 1
        return res