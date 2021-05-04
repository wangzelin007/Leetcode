# 给定二叉搜索树的根结点root，返回值位于范围 [low, high] 之间的所有结点的值的和。
# 示例 1：
# 输入：root = [10,5,15,3,7,null,18], low = 7, high = 15
# 输出：32
# 示例 2：
# 输入：root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# 输出：23
# 提示：
# 树中节点数目在范围 [1, 2 * 104] 内
# 1 <= Node.val <= 105
# 1 <= low <= high <= 105
# 所有 Node.val 互不相同
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/range-sum-of-bst
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for a binary tree node.
from bisect import bisect_left

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 笨办法
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.res = []
        self.dfs(root)
        l = bisect_left(self.res, low)
        r = bisect_left(self.res, high)
        return sum(self.res[l:r+1])

    def dfs(self, root):
        if not root: return
        self.dfs(root.left)
        self.res.append(root.val)
        self.dfs(root.right)

# DFS
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        # 三个return 不能少呀
        if not root: return 0
        if root.val > high: return self.rangeSumBST(root.left, low, high)
        if root.val < low: return self.rangeSumBST(root.right, low, high)
        # 这一行卡住了，肯定是中左右的值都要， 上面两个判断会进行剪枝
        else: return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

# 好理解
class Solution(object):
    def rangeSumBST(self, root, low, high):
        res = 0
        if not root:
            return res
        if root.val > low:
            res += self.rangeSumBST(root.left, low, high)
        if low <= root.val <= high:
            res += root.val
        if root.val < high:
            res += self.rangeSumBST(root.right, low, high)
        return res

from collections import deque
# BFS
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        q = deque([root])
        res = 0
        while q:
            node = q.popleft()
            if not node: continue
            if node.val < low: q.append(node.right)
            elif node.val > high: q.append(node.left)
            else:
                res += node.val
                q.append(node.left)
                q.append(node.right)
        return res
