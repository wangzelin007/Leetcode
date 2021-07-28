# 给定一个二叉树（具有根结点root），一个目标结点target，和一个整数值 K 。
# 返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。
# 示例 1：
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
# 输出：[7,4,1]
# 解释：
# 所求结点为与目标结点（值为 5）距离为 2 的结点，
# 值分别为 7，4，以及 1
# 注意，输入的 "root" 和 "target" 实际上是树上的结点。
# 上面的输入仅仅是对这些对象进行了序列化描述。

# 提示：
# 给定的树是非空的。
# 树上的每个结点都具有唯一的值 0 <= node.val <= 500。
# 目标结点target是树上的结点。
# 0 <= K <= 1000.

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 1. 标记所有 node 的父节点
# 2. dfs 查找所有 == k 难点：向上找怎么实现？
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.parent_relation = {}
        self.visited = set()
        self.k = k
        self.ans = []
        self.mark_parents(root, None)
        self.get_knodes(target, 0)
        return self.ans

    def mark_parents(self, node, parent):
        if not node:
            return
        self.parent_relation[node.val] = parent
        self.mark_parents(node.left, node)
        self.mark_parents(node.right, node)

    def get_knodes(self, node, level):
        if not node or node.val in self.visited:
            return
        if node and level == self.k:
            self.ans.append(node.val)
            return
        self.visited.add(node.val)
        self.get_knodes(node.left, level+1)
        self.get_knodes(node.right, level+1)
        self.get_knodes(self.parent_relation[node.val], level+1)

def test():
    # root = [3,5,1,6,2,0,8,null,null,7,4]
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    s = Solution()
    print(s.distanceK(root, root.left, 2))

if __name__ == '__main__':
    test()