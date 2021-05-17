# 在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。
# 如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。
# 我们给出了具有唯一值的二叉树的根节点 root ，以及树中两个不同节点的值 x 和 y 。
# 只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true 。否则，返回 false。
# 示例 1：
# 输入：root = [1,2,3,4], x = 4, y = 3
# 输出：false
# 示例 2：
# 输入：root = [1,2,3,null,4,null,5], x = 5, y = 4
# 输出：true
# 示例 3：
# 输入：root = [1,2,3,null,4], x = 2, y = 3
# 输出：false
# 提示：
# 二叉树的节点数介于2 到100之间。
# 每个节点的值都是唯一的、范围为1 到100的整数。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/cousins-in-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# dfs
class Solution1:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_parent, x_depth, x_found = None, None, False
        y_parent, y_depth, y_found = None, None, False

        def dfs(node: TreeNode, depth: int, parent: TreeNode):
            if not node: return
            # nonlocal关键字修饰变量后，标识该变量是上一级函数中的局部变量。
            nonlocal x_parent, y_parent, x_depth, y_depth, x_found, y_found

            if node.val == x:
                x_parent, x_depth, x_found = parent, depth, True
            elif node.val == y:
                y_parent, y_depth, y_found = parent, depth, True

            if x_found and y_found:
                return

            dfs(node.left, depth + 1, node)

            if x_found and y_found:
                return

            dfs(node.right, depth + 1, node)

        dfs(root, 0, None)
        return x_depth == y_depth and x_parent == y_parent

import collections
# bfs
class Solution2:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_parent, x_depth, x_found = None, None, False
        y_parent, y_depth, y_found = None, None, False

        def update(node: TreeNode, parent: TreeNode, depth: int):
            if node.val == x:
                # nonlocal关键字修饰变量后，标识该变量是上一级函数中的局部变量。
                nonlocal x_parent, x_depth, x_found
                x_parent, x_depth, x_found = parent, depth, True
            elif node.val == y:
                nonlocal y_parent, y_depth, y_found
                y_parent, y_depth, y_found = parent, depth, True

        q = collections.deque([(root, 0)])
        update(root, None, 0)
        while q:
            node, depth = q.popleft()
            if node.left:
                q.append((node.left, depth + 1))
                update(node.left, node, depth + 1)
            if node.right:
                q.append((node.right, depth + 1))
                update(node.right, node, depth + 1)

            if x_found and y_found:
                break

        return x_depth == y_depth and x_parent != y_parent