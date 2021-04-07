# 请实现一个函数，用来判断一棵二叉树是不是对称的。
# 如果一棵二叉树和它的镜像一样，那么它是对称的。
# 例如，二叉树[1,2,2,3,4,4,3] 是对称的。
#
#    1
#   / \
#  2   2
# / \ / \
# 3 4 4  3
# 但是下面这个[1,2,2,null,3,null,3] 则不是镜像对称的:
#  1
# / \
# 2  2
#  \  \
#   3  3
#
# 示例 1：
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
# 示例 2：
# 输入：root = [1,2,2,null,3,null,3]
# 输出：false
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 对称二叉树定义：
# 对于树中任意两个对称节点L、R，一定有：
# 1. L.val = R.val
# 2. L.left.val = R.right.val
# 3. L.right.val = R.left.val
#
# isSymmetric(root):
# 特例：若根root为空，返回True
# 返回：recur(root.left, root.right)
# recur(L, R):
# 终止条件：
# 1. 当L和R同时越过叶子节点时，返回True
# 2. 当L和R只有一个越过叶子节点时，返回False
# 3. 当L.val != R.val时，返回False
# 递归工作：
# recur(L.left, R.right)
# recur(L.right, R.left)
# 返回值：
# and 连接

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.recur(root.left, root.right)

    def recur(self, A, B):
        if not A and not B: return True
        if (A and not B) or (B and not A): return False
        if A.val != B.val: return False
        return self.recur(A.left, B.right) and self.recur(A.right, B.left)
