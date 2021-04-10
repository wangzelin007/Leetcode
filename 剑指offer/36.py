# _*_ coding: utf-8 _*_
# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。
# 要求不能创建任何新的节点，只能调整树中节点指针的指向。
# 为了让您更好地理解问题，以下面的二叉搜索树为例：
#     4
#    / \
#   2   5
#  / \
# 1   3
# 我们希望将这个二叉搜索树转化为双向循环链表。
# 链表中的每个节点都有一个前驱和后继指针。
# 对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。
# 下图36.png展示了上面的二叉搜索树转化成的链表。
# “head” 表示指向链表中有最小元素的节点。
# 特别地，我们希望可以就地完成转换操作。
# 当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。
# 还需要返回链表中的第一个节点的指针。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 解题思路：
# 本文解法基于性质：二叉搜索树的中序遍历为 递增序列 。
# 将 二叉搜索树 转换成一个 “排序的循环双向链表” ，其中包含三个要素：
# 排序链表： 节点应从小到大排序，因此应使用 中序遍历 “从小到大”访问树的节点。
# 双向链表： 在构建相邻节点的引用关系时，设前驱节点 pre 和当前节点 cur ，不仅应构建 pre.right = cur ，也应构建 cur.left = pre 。
# 循环链表： 设链表头节点 head 和尾节点 tail ，则应构建 head.left = tail 和 tail.right = head 。
#
# 算法流程：
# dfs(cur): 递归法中序遍历；
# 终止条件： 当节点 cur 为空，代表越过叶节点，直接返回；
# 递归左子树，即 dfs(cur.left) ；
# 构建链表：
# 当 pre 为空时： 代表正在访问链表头节点，记为 head ；
# 当 pre 不为空时： 修改双向节点引用，即 pre.right = cur ， cur.left = pre ；
# 保存 cur ： 更新 pre = cur ，即节点 cur 是后继节点的 pre ；
# 递归右子树，即 dfs(cur.right) ；
#
# treeToDoublyList(root)：
# 特例处理： 若节点 root 为空，则直接返回；
# 初始化： 空节点 pre ；
# 转化为双向链表： 调用 dfs(root) ；
# 构建循环链表： 中序遍历完成后，head 指向头节点， pre 指向尾节点，因此修改 head 和 pre 的双向节点引用即可；
# 返回值： 返回链表的头节点 head 即可；
#
# 复杂度分析：
# 时间复杂度 O(N) ： N 为二叉树的节点数，中序遍历需要访问所有节点。
# 空间复杂度 O(N) ： 最差情况下，即树退化为链表时，递归深度达到 N，系统使用 O(N) 栈空间。
#
# 作者：jyd
# 链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/solution/mian-shi-ti-36-er-cha-sou-suo-shu-yu-shuang-xian-5/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def dfs(cur):
            if not cur: return
            dfs(cur.left)
            if self.pre:
                self.pre.right, cur.left = cur, self.pre
            else:
                self.head = cur
            self.pre = cur # 更新pre位置
            dfs(cur.right)
        if not root: return
        self.pre = None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head
