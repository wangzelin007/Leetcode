# _*_ coding: utf-8 _*_
# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
# 注意：本题与 530：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/ 相同
#
# 示例 1：
# 输入：root = [4,2,6,1,3]
# 输出：1
#
# 示例 2：
# 输入：root = [1,0,48,null,null,12,49]
# 输出：1
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 中序遍历 从小到大
        def dfs(root):
            if not root: return
            dfs(root.left)
            if self.pre != -1:
                self.res = min(self.res, root.val - self.pre)
            self.pre = root.val
            dfs(root.right)
        self.res = float('inf')
        # self.pre = None 会导致0失效
        self.pre = -1
        dfs(root)
        return self.res

    def dfs_mlr(self, root):
        if not root: return
        print root.val,
        self.dfs_mlr(root.left)
        self.dfs_mlr(root.right)

    def dfs_lmr(self, root):
        if not root: return
        self.dfs_lmr(root.left)
        print root.val,
        self.dfs_lmr(root.right)

    def dfs_lrm(self, root):
        if not root: return
        self.dfs_lrm(root.left)
        self.dfs_lrm(root.right)
        print root.val,




if __name__ == '__main__':
    # [90,69,null,49,89,null,52]
    s = Solution()
    # [0,null,2236,1277,2776,519]
    root = TreeNode(0)
    root.right = TreeNode(2236)
    root.right.left = TreeNode(1277)
    root.right.right = TreeNode(2776)
    root.right.left.left = TreeNode(519)
    # root = TreeNode(4)
    # root.left = TreeNode(2)
    # root.right = TreeNode(6)
    # root.left.left = TreeNode(1)
    # root.left.right = TreeNode(3)
    # root.right.left = TreeNode(5)
    # root.right.right = TreeNode(7)
    print(s.minDiffInBST(root))
      #  4
     # 2   6
    # 1 3 5 7ss
    s.dfs_mlr(root)
    print '\n'
    s.dfs_lmr(root)
    print '\n'
    s.dfs_lrm(root)
    print '\n'

