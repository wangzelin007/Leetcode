# 从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
# 例如:
# 给定二叉树:[3,9,20,null,null,15,7],
#   3
#  / \
# 9  20
#    / \
#   15  7
# 返回：
# [3,9,20,15,7]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 其实是按层打印，又称为二叉树的 广度优先搜索（BFS）。
# BFS 通常借助 队列 的先入先出特性来实现。
# 算法流程：
# 1. 特例处理：root 为空，return []
# 2. 初始化：q 包含root 的collections.deque(), res []
# 3. BFS 循环：当 q 为空时跳出
#     1. 出队：队首元素出队，并记为root
#     2. 打印：将root.val 追加到 res
#     3. 添加子节点：如果root的左/右节点不为空，追加root的左/右节点到q中。
# 4. 返回值：res
#
# 复杂度分析：
# 时间复杂度 O(N) ： N 为二叉树的节点数量，即 BFS 需循环 N 次。
# 空间复杂度 O(N) ： 最差情况下，即当树为平衡二叉树时，最多有 N/2 个树节点同时在 queue 中，使用 O(N) 大小的额外空间。

from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        q, res = deque(), []
        q.append(root)
        while q:
            root = q.popleft()
            res.append(root.val)
            if root.left: q.append(root.left)
            if root.right: q.append(root.right)
        return res

