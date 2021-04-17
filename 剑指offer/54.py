# 给定一棵二叉搜索树，请找出其中第k大的节点。
# 示例 1:
# 输入: root = [3,1,4,null,2], k = 1
#   3
#  / \
# 1   4
#  \
#   2
# 输出: 4
# 示例 2:
# 输入: root = [5,3,6,2,4,null,null,1], k = 3
#       5
#      / \
#     3   6
#    / \
#   2   4
#  /
# 1
# 输出: 4
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 中序遍历
class Solution1:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            if not root: return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        res = []
        dfs(root)
        print(res)
        return res[-k]

# 优化 右中左 且访问K次
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            if not root: return
            dfs(root.right)
            if self.k == 0: return
            self.k -= 1
            if self.k == 0:
                self.res = root.val
            dfs(root.right)
        self.k = k
        dfs(root)
        return self.res

