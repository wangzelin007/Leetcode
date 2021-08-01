from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 104 最大深度
    # DFS
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # BFS
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        queue = deque()
        queue.append(root)
        while queue:
            res += 1
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res

    # 111 最小深度
    # DFS
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftmin = self.minDepth(root.left)
        rightmin = self.minDepth(root.right)
        if leftmin == 0 or rightmin == 0:
            return 1 + leftmin + rightmin
        else:
            return 1 + min(leftmin, rightmin)
    # BFS
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        queue = deque()
        queue.append(root)
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if not node.left and not node.right:
                    return res + 1
            res += 1