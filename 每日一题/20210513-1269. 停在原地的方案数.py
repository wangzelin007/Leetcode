# dp
# 有一个长度为arrLen的数组，开始有一个指针在索引0 处。
# 每一步操作中，你可以将指针向左或向右移动 1 步，或者停在原地（指针不能被移动到数组范围外）。
# 给你两个整数steps 和arrLen ，请你计算并返回：在恰好执行steps次操作以后，指针仍然指向索引0 处的方案数。
# 由于答案可能会很大，请返回方案数 模10^9 + 7 后的结果。
# 示例 1：
# 输入：steps = 3, arrLen = 2
# 输出：4
# 解释：3 步后，总共有 4 种不同的方法可以停在索引 0 处。
# 向右，向左，不动
# 不动，向右，向左
# 向右，不动，向左
# 不动，不动，不动
# 示例 2：
# 输入：steps = 2, arrLen = 4
# 输出：2
# 解释：2 步后，总共有 2 种不同的方法可以停在索引 0 处。
# 向右，向左
# 不动，不动
# 示例 3：
# 输入：steps = 4, arrLen = 2
# 输出：8
# 提示：
# 1 <= steps <= 500
# 1 <= arrLen<= 10^6
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# dp[i] = dp[i] + dp[i-1] + dp[i+1]

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10**9 + 7
        maxColumn = min(arrLen - 1, steps // 2 + 1)

        dp = [0] * (maxColumn + 1)
        dp[0] = 1

        for i in range(1, steps + 1):
            dpNext = [0] * (maxColumn + 1)
            for j in range(0, maxColumn + 1):
                dpNext[j] = dp[j]
                if j - 1 >= 0:
                    dpNext[j] = (dpNext[j] + dp[j - 1]) % mod
                if j + 1 <= maxColumn:
                    dpNext[j] = (dpNext[j] + dp[j + 1]) % mod
            dp = dpNext

        return dp[0]

# class Solution:
#     def numWays(self, steps: int, arrLen: int) -> int:
#         arrLen = min(steps // 2 + 1, arrLen)
#         dp = [1] + [0] * (arrLen - 1)
#         mod = 1000000007
#         for _ in range(steps):
#             s = [0] * arrLen
#             s[0] = (dp[0] + dp[1]) % mod
#             s[-1] = (dp[-1] + dp[-2]) % mod
#             for j in range(1, arrLen-1):
#                 s[j] = (dp[j-1] + dp[j] + dp[j+1]) % mod
#             dp = s.copy()
#         return dp[0]

import functools

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @functools.lru_cache(None)
        def dfs(pos,c):
            if c==steps and pos == 0:
                return 1
            if c==steps and pos!=0:
                return 0
            res = 0
            if pos==0:
                for i in [0,1]:
                    res+=dfs(pos+i,c+1)
            elif pos == arrLen-1:
                for i in [0,-1]:
                    res+=dfs(pos+i,c+1)
            else:
                for i in [-1,0,1]:
                    res+=dfs(pos+i,c+1)
            return res
        return dfs(0,0)%(10**9 + 7)