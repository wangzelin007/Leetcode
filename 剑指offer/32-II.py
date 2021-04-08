# 从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
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
#     [9,20],
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
        stack, res = deque(), []
        stack.append(root)
        while stack:
            tmp = []
            for i in range(len(stack)):
                root = stack.popleft()
                tmp.append(root.val)
                if root.left: stack.append(root.left)
                if root.right: stack.append(root.right)
            res.append(tmp)
        return res
