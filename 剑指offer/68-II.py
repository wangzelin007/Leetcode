# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，
# 最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
# 例如，给定如下二叉树: root =[3,5,1,6,2,0,8,null,null,7,4]
# 示例 1:
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
# 示例2:
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 2021-04-24 完结撒花 目标王者段位
# 最近公共祖先root满足：
# 1. p q 位于root的异侧
# 2. 或者p q本身就是公共祖先
#      3
#    5   1
#   6 2 0 8
#    7 4

# 理解难点：回溯 比如我们找0和8
# 我们知道此时是dfs，会优先一路找到最左侧6。
# 此时会触发 not root 条件，return root(None) 即 root 表示的是 上一层的 root.left
# 那么会找 root.right 2, 会依次找 7 和 4,return None
# 一直回溯到3.left的结果为None
# ------------------- 3.left 左子树搜索完毕
# 开始寻找3.right
# 1.left -> 0 return 0 (left=0; root=1)
# 1.right -> 8 return 8 (right=8; root=1)
# return 1 找到
# ------------------- 分析找 1 0 包含的情况
# 3.left = None (left=None, root=3)
# 3.right = 1 retrun 1 (right=1，root=3)
# return right 即 1 找到了

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q : return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: return right
        if not right: return left
        return root
