# 输入一棵二叉树的根节点，求该树的深度。
# 从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7]，
#       3
#      / \
#     9  20
#        / \
#      15   7
# 返回它的最大深度3 。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# DFS
# 算法解析：
# 终止条件： 当 root 为空，说明已越过叶节点，因此返回 深度 0 。
# 递推工作： 本质上是对树做后序遍历。
# 计算节点 root 的 左子树的深度 ，即调用 maxDepth(root.left)；
# 计算节点 root 的 右子树的深度 ，即调用 maxDepth(root.right)；
# 返回值： 返回 此树的深度 ，即 max(maxDepth(root.left), maxDepth(root.right)) + 1。

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# BFS
# 树的层序遍历 / 广度优先搜索往往利用 队列 实现。
# 关键点： 每遍历一层，则计数器 +1 ，直到遍历完成，则可得到树的深度。
# 算法解析：
# 特例处理： 当 root 为空，直接返回 深度 0 。
# 初始化： 队列 queue （加入根节点 root ），计数器 res = 0。
# 循环遍历： 当 queue 为空时跳出。
# 初始化一个空列表 tmp ，用于临时存储下一层节点；
# 遍历队列： 遍历 queue 中的各节点 node ，并将其左子节点和右子节点加入 tmp；
# 更新队列： 执行 queue = tmp ，将下一层节点赋值给 queue；
# 统计层数： 执行 res += 1 ，代表层数加 1；
# 返回值： 返回 res 即可。
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        res, queue = 0, [root]
        if not root: return 0
        while queue:
            tmp = []
            for node in queue:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            queue = tmp
            res += 1
        return res