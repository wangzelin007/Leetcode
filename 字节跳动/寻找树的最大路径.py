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
        print('recur:', root.data if root else None)
        if not root:
            return 0
        left = self.findMaxPathRecur(root.lchild)
        right = self.findMaxPathRecur(root.rchild)
        # print(left, right)
        # res 和 左、右最大值的和比较
        print('res:', self.res, left + right)
        self.res = max(self.res, left + right)
        print('return max + 1:', left, right)
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
      # 1
    # 2   3
   # 4 5   7
  # 6
# 所以通过日志可以看出递归的调用：

# 1
# 1.l
# 2.l
# 4.l
# 6.l
# 6.r
# 更新res = 0
# return 6.len = 1 作为4.l 比如 left=4.l=6=6.l+6.r+1
# 4.r
# 更新res = 1
# return 4.len = 2 作为2.l
# 2.r
# 5.l
# 5.r
# 更新res = 1
# return 5.len = 1 作为2.r
# 更新res = 3
# return 2.len = 3 作为1.l
# 1.r
# 3.l
# 3.r
# 7.l
# 7.r
# 更新res = 3
# return 7.len = 1 作为3.r
# 更新res = 3
# return 3.len = 2 作为1.r
# 更新res = 5
# return 1.len = 4 作为上一个节点的左/右？
# ('recur:', 1)
# ('recur:', 1.l = 2)
# ('recur:', 2.l = 4)
# ('recur:', 4.l = 6)
# ('recur:', 6.l = None)
# ('recur:', 6.r = None)
# ('更新节点6的 res:', self.res: 0, 6.l+6.r: 0)
# ('return 到6的路径长度', max(0, 0) + 1)
# ('recur:', 4.r = None)
# ('更新节点4的 res:', self.res: 0, 4.l+4.r: 1)
# ('return 到4的路径长度:', max(1, 0) + 1
# ('recur:', 2.r = 5)
# ('recur:', 5.l = None)
# ('recur:', 5.r = None)
# ('更新到节点5的 res:', self.res: 1, 5.l+5.r: 0)
# ('return 到5的路径长度:', max(0, 0) + 1
# ('更新到节点2的 res:', self.res: 1, 2.l+2.r: 3)
# ('return 到2的路径长度:', max(2, 1) + 1
# ('recur:', 1.r = 3)
# ('recur:', 3.l = None)
# ('recur:', 3.r = 7)
# ('recur:', 7.l = None)
# ('recur:', 7.r = None)
# ('更新到节点7的 res:', self.res: 3, 7.l+7.r: 0)
# ('return 到7的路径长度:', max(0, 0) + 1
# ('更新到节点3的 res:', self.res: 3, 3.l+3.r: 1)
# ('return 到3的路径长度:', max(0, 1) + 1
# ('更新到节点1的 res:', self.res: 3, 1.l+1.r: 5)
# ('return 到1的路径长度:', max(3, 2) + 1