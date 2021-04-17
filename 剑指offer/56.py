# 输入一棵二叉树的根节点，判断该树是不是平衡二叉树。
# 如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
# 示例 1:
# 给定二叉树 [3,9,20,null,null,15,7]
#       3
#      / \
#     9  20
#        / \
#      15   7
# 返回 true 。
# 示例 2:
# 给定二叉树 [1,2,2,3,3,null,null,4,4]
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 算法流程：
# isBalanced(root) 函数： 判断树 root 是否平衡
# 特例处理： 若树根节点 root 为空，则直接返回 true；
# 返回值： 所有子树都需要满足平衡树性质，因此以下三者使用与逻辑 and 连接；
# abs(self.depth(root.left) - self.depth(root.right)) <= 1 ：判断 当前子树 是否是平衡树；
# self.isBalanced(root.left) ： 先序遍历递归，判断 当前子树的左子树 是否是平衡树；
# self.isBalanced(root.right) ： 先序遍历递归，判断 当前子树的右子树 是否是平衡树；
# depth(root) 函数： 计算树 root 的深度
# 终止条件： 当 root 为空，即越过叶子节点，则返回高度 0 ；
# 返回值： 返回左 / 右子树的深度的最大值 +1 。
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and\
               self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root: return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1

# 算法流程：
# recur(root) 函数：
# 返回值：
# 当节点root 左 / 右子树的深度差 ≤1 ：则返回当前子树的深度，
# 即节点 root 的左 / 右子树的深度最大值 +1 （ max(left, right) + 1 ）；
# 当节点root 左 / 右子树的深度差 >2 ：则返回 −1 ，代表 此子树不是平衡树 。
# 终止条件：
# 当 root 为空：说明越过叶节点，因此返回高度 0 ；
# 当左（右）子树深度为 −1 ：代表此树的 左（右）子树 不是平衡树，因此剪枝，直接返回 −1 ；
# isBalanced(root) 函数：
# 返回值： 若 recur(root) != -1 ，则说明此树平衡，返回 true ； 否则返回 false 。
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def recur(root):
            if not root: return 0
            left = recur(root.left)
            if left == -1: return -1
            right = recur(root.right)
            if right == -1: return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1
        return recur(root) != -1
