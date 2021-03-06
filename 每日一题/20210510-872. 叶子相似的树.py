# 请考虑一棵二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个叶值序列 。
# 举个例子，如上图所示，给定一棵叶值序列为(6, 7, 4, 9, 8)的树。
# 如果有两棵二叉树的叶值序列是相同，那么我们就认为它们是叶相似的。
# 如果给定的两个根结点分别为root1 和root2的树是叶相似的，则返回true；否则返回 false 。
# 示例 1：
# 输入：root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# 输出：true
# 示例 2：
# 输入：root1 = [1], root2 = [1]
# 输出：true
# 示例 3：
# 输入：root1 = [1], root2 = [2]
# 输出：false
# 示例 4：
# 输入：root1 = [1,2], root2 = [2,2]
# 输出：true
# 示例 5：
# 输入：root1 = [1,2,3], root2 = [1,3,2]
# 输出：false
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/leaf-similar-trees
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        res1 = []
        res2 = []
        self.dfs(root1, res1)
        self.dfs(root2, res2)
        return res1 == res2

    def dfs(self, root, result):
        if root is None:
            return
        if root.left is None and root.right is None:
            result.append(root.val)
        self.dfs(root.left, result)
        self.dfs(root.right, result)


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node: TreeNode):
            if not node.left and not node.right:
                yield node.val
            else:
                if node.left:
                    yield from dfs(node.left)
                if node.right:
                    yield from dfs(node.right)

        seq1 = list(dfs(root1)) if root1 else list()
        seq2 = list(dfs(root2)) if root2 else list()
        return seq1 == seq2

