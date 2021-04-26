# 在一座城市里，你需要建 n 栋新的建筑。
# 这些新的建筑会从 1 到 n 编号排成一列。
# 这座城市对这些新建筑有一些规定：
# 每栋建筑的高度必须是一个非负整数。
# 第一栋建筑的高度 必须 是 0 。
# 任意两栋相邻建筑的高度差 不能超过  1 。
# 除此以外，某些建筑还有额外的最高高度限制。
# 这些限制会以二维整数数组 restrictions 的形式给出，其中 restrictions[i] = [idi, maxHeighti] ，表示建筑 idi 的高度 不能超过 maxHeighti 。
# 题目保证每栋建筑在 restrictions 中 至多出现一次 ，同时建筑 1 不会 出现在 restrictions 中。
# 请你返回 最高 建筑能达到的 最高高度 。
# 示例 1：
# 输入：n = 5, restrictions = [[2,1],[4,1]]
# 输出：2
# 解释：上图中的绿色区域为每栋建筑被允许的最高高度。
# 我们可以使建筑高度分别为 [0,1,2,1,2] ，最高建筑的高度为 2 。
# 示例 2：
# 输入：n = 6, restrictions = []
# 输出：5
# 解释：上图中的绿色区域为每栋建筑被允许的最高高度。
# 我们可以使建筑高度分别为 [0,1,2,3,4,5] ，最高建筑的高度为 5 。
# 示例 3：
# 输入：n = 10, restrictions = [[5,3],[2,5],[7,4],[10,3]]
# 输出：5
# 解释：上图中的绿色区域为每栋建筑被允许的最高高度。
# 我们可以使建筑高度分别为 [0,1,2,3,3,4,4,5,4,3] ，最高建筑的高度为 5 。
# 提示：
# 2 <= n <= 109
# 0 <= restrictions.length <= min(n - 1, 105)
# 2 <= idi <= n
# idi 是 唯一的 。
# 0 <= maxHeighti <= 109

# 推导过程：https://leetcode-cn.com/problems/maximum-building-height/solution/zui-gao-jian-zhu-gao-du-by-leetcode-solu-axbb/
# (i, hi) 代表建筑i的高度不能超过hi
# 因此:
# 1. i-1 不能超过 hi+1；i+1 不能超过 hi+1
# 2. j 的高度不能超过 hi + |j-i|
# 3. 我们可以将每一个限制r传递开来，得到r[i][1]
# 4. 如果i j 之间没有限制r, 那么他们应该像一座山脉一样，先递增到最大值，再递减回到边界值。
# 所以得出推导公式：
# best(i,j) - r[i][1] + best(i,j) - r[j][1] <= r[j][0] - r[i][0]
# 所以：
# best(i,j) = (r[i][1] + r[j][1] + r[j][0] - r[i][0]) // 2

class Solution(object):
    def maxBuilding(self, n, r):
        r.append([1, 0]) # 添加题目给出的第一个限制
        r.sort()
        if r[-1][0] != n: # 判断如果没有最后一个限制，加上最后一个限制。
            r.append([n, n-1]) # 即使一直递增也满足 <= n-1
        k = len(r) # 是对相隔的r做循环，非常重要
        res = 0
        for i in range(1, k): # 从左到右传递
            r[i][1] = min(r[i][1], r[i - 1][1] + r[i][0] - r[i - 1][0]) # 上坡
        for i in range(k - 2, -1, -1): # 从右到左传递
            r[i][1] = min(r[i][1], r[i + 1][1] + r[i + 1][0] - r[i][0]) # 下坡
        for i in range(k-1): # 对每个区间求值，并取最大值
            best = (r[i+1][1] + r[i][1] + r[i+1][0] - r[i][0]) // 2
            res = max(res, best)
        return res

if __name__ == '__main__':
    s = Solution()
    n = 5; restrictions = [[2,1],[4,1]]
    # n = 6; restrictions = []
    # n = 10; restrictions = [[5,3],[2,5],[7,4],[10,3]]
    s.maxBuilding(n, restrictions)