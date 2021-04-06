# 输入两棵二叉树A和B，判断B是不是A的子结构。
# (约定空树不是任意一个树的子结构)
# B是A的子结构， 即 A中有出现和B相同的结构和节点值。
#
# 例如:
# 给定的树 A:
#     3
#    / \
#   4  5
#  / \
# 1   2
# 给定的树 B：
#   4
#  /
# 1
# 返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。
#
# 示例 1：
# 输入：A = [1,2,3], B = [3,1]
# 输出：false
#
# 示例 2：
# 输入：A = [3,4,5,1,2], B = [4,1]
# 输出：true

# 说明：节点A代表树A的根结点，节点B代表树B的根结点
# recur(A, B)函数：判断树A是否等于树B
# 1.终止条件：
#   a. 节点B为空：说明树B已经遍历完成，越过了叶子节点。返回True
#   b. 节点A为空：说明树A已经遍历完成，越过了叶子节点。返回False
#   c. A.val != B.val，返回False
# 2.返回值：
#   a. 判断A和B的左节点是否相等，recur(A.left, B.left)
#   b. 判断A和B的右节点是否相等，recur(A.right, B.right)
# isSubStructure(A, B)函数：判断树B是否树A的子结构
# 1.特例处理：当树A为空或者树B为空时，返回False
# 2.返回值：如果树B是树A的子结构，必须满足如下三种情况：
#   a. 树A等于树B recur(A, B)
#   b. 树B是树A左子树的子结构 isSubStructure(A.left, B)
#   c. 树B是树A右子树的子结构 isSubStructure(A.right, B)

class Solution:
    def isSubStructure(self, A, B):
        if not A or not B: return False
        return self.recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def recur(self, A, B):
        if not B: return True
        if not A: return False
        if A.val != B.val: return False
        return self.recur(A.left and B.left) and self.recur(A.right and B.right)
