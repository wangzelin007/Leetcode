# _*_ coding: utf-8 _*_
# 264.丑数II
# 给你一个整数 n ，请你找出并返回第 n 个 丑数 。
# 丑数 就是只包含质因数2、3 和/或5的正整数。
# 示例 1：
# 输入：n = 10
# 输出：12
# 解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。
#
# 示例 2：
# 输入：n = 1
# 输出：1
# 解释：1 通常被视为丑数。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/ugly-number-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 动态规划 dp[i] = min(dp[p2]*2,dp[p3]*3,dp[p5]*5)
class Solution1(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[1] = 1
        p2 = p3 = p5 = 1
        for i in range (2,n+1):
            num2, num3, num5 = dp[p2]*2, dp[p3]*3, dp[p5]*5
            dp[i] = min(num2, num3, num5)
            if dp[i] == num2: p2 += 1
            if dp[i] == num3: p3 += 1
            if dp[i] == num5: p5 += 1
        return dp[n]

# 最小堆，add 堆顶元素 *2 *3 *5
# 需要set进行去重
import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        dic = {1}
        heap = [1]
        factors = [2,3,5]
        for i in range(n-1):
            cur = heapq.heappop(heap)
            for factor in factors:
                nxt = factor * cur
                if nxt not in dic:
                    dic.add(nxt)
                    heapq.heappush(heap, nxt)
        return heapq.heappop(heap)

if __name__ == '__main__':
    s = Solution()
    print(s.nthUglyNumber(20)) # 36