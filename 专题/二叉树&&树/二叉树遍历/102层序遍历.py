from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            current_level = []
            current_size = len(queue)
            for i in range(current_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                current_level.append(node.val)
            res.append(current_level)
        return res

    # DFS
    def leverOrder2(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        self.res = []
        self._dfs(root, 0)
        return self.res

    def _dfs(self, node, level):
        if not node:
            return
        if len(self.res) == level:
            self.res.append([])
        self.res[level].append(node.val)
        self._dfs(node.left, level+1)
        self._dfs(node.right, level+1)





