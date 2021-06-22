# coding: utf-8
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

# 1.退出条件 not root
# 2.递归函数的作用就是找最大深度
class Solution:
    def __init__(self):
        self.res = 0

    def findMaxPath(self, root):
        if not root: return 0
        self.findMaxPathRecur(root)
        return self.res

    def findMaxPathRecur(self, root):
        if not root:
            return 0
        left = self.findMaxPathRecur(root.lchild)
        right = self.findMaxPathRecur(root.rchild)
        # print(left, right)
        # res 和 左、右最大值的和比较
        self.res = max(self.res, left + right)
        return max(left, right) + 1

if __name__ == '__main__':
    root = TreeNode(1)
    root.lchild = TreeNode(2)
    root.rchild = TreeNode(3)
    root.lchild.lchild = TreeNode(4)
    root.lchild.rchild = TreeNode(5)
    root.lchild.lchild.lchild = TreeNode(6)
    root.rchild.rchild = TreeNode(7)
    s = Solution()
    print(s.findMaxPath(root))