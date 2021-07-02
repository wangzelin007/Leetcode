# offer 33
# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。
# 如果是则返回 true，否则返回 false。
# 假设输入的数组的任意两个数字都互不相同。

# 后序遍历定义： [ 左子树 | 右子树 | 根节点 ] ，即遍历顺序为 “左、右、根” 。
# 二叉搜索树定义：
# 左子树中所有节点的值 << 根节点的值；
# 右子树中所有节点的值 >> 根节点的值；
# 其左、右子树也分别为二叉搜索树。

# 根据二叉搜索树的性质，采用递归分治思想，递归的判断所有子树的正确性。
# 递归解析：
# 终止条件： 当 i≥j ，说明此子树节点数量 ≤1 ，无需判别正确性，因此直接返回 true；
# 递推工作：
# 划分左右子树： 遍历后序遍历的 [i,j] 区间元素，寻找 第一个大于根节点 的节点，索引记为 m 。
# 此时，可划分出左子树区间 [i,m−1] 、右子树区间 [m,j−1] 、根节点索引 j 。
# 判断是否为二叉搜索树：
# 左子树区间 [i,m−1] 内的所有节点都应 <postorder[j] 。
# 而划分左右子树 步骤已经保证左子树区间的正确性，因此只需要判断右子树区间即可。
# 右子树区间 [m,j−1] 内的所有节点都应 >postorder[j] 。
# 实现方式为遍历，当遇到 ≤postorder[j] 的节点则跳出；
# 则可通过 p=j 判断是否为二叉搜索树。即跳出节点就是j本身。
# 返回值： 所有子树都需正确才可判定正确，因此使用 与逻辑符 && 连接。
# p=j ： 判断 此树 是否正确。
# recur(i,m−1) ： 判断 此树的左子树 是否正确。
# recur(m,j−1) ： 判断 此树的右子树 是否正确。
# O(N^2) && 0(N)
# 左右中
class Solution1(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        def recur(i,j):
            if i >= j: return True
            p = i
            while postorder[p] < postorder[j]: p += 1
            m = p
            while postorder[p] > postorder[j]: p += 1
            return p == j and recur(i,m-1) and recur(m,j-1)
        return recur(0,len(postorder)-1)

# 辅助单调栈
# 后续遍历为 左右中，我们倒序检查 中右左。
#      4
#    2   6
#   1 3 5 7
# [1 3 2 5 7 6 4] 左右中
# [4 6 7 5 2 3 1] 中右左
# [1 3 2 7 5 6 4] 错误
class Solution2:
    def verifyPostorder(self, postorder: [int]) -> bool:
        stack, root = [], float("+inf")
        for i in range(len(postorder) - 1, -1, -1): # 倒序检查
            # 整颗树也看做root的左孩子，任何左孩子都应该 < root,对于大于 root 的情况：False。
            if postorder[i] > root: return False
            while(stack and postorder[i] < stack[-1]): # 发现左，右、中出栈，最后root为中
                root = stack.pop()
            stack.append(postorder[i]) # 中右入栈
        return True

if __name__ == '__main__':
    s1 = Solution1()
    print(s1.verifyPostorder([1,3,2,7,5,6,4]))
    s2 = Solution2()
    print(s2.verifyPostorder([1,3,2,5,7,6,4]))
    # print(s2.verifyPostorder([1,3,2,7,5,6,4]))

