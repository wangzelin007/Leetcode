# 请完成一个函数，输入一个二叉树，该函数输出它的镜像。
# 例如输入：
#
#      4
#    /   \
#   2     7
#  / \   /  \
# 1   3 6    9
# 镜像输出：
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
#
# 示例 1：
# 输入：root = [4,2,7,1,3,6,9]
# 输出：[4,7,2,9,6,3,1]

# 前序遍历
# mirrorTree函数：镜像root
# 退出条件：root为空，已经遍历完所有的叶子节点，返回空
# 返回值：如果需要镜像需要三步骤
# 1.root 的左子树镜像完成
# 2.root 的右子树镜像完成
# 3.root 的左右子树交换位置

class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return
        left = self.mirrorTree(root.left)
        right = self.mirrorTree(root.right)
        root.left, root.right = right, left
        return root