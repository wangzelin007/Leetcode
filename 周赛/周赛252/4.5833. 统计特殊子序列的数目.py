# 特殊序列 是由 正整数 个 0 ，紧接着 正整数 个 1 ，最后 正整数 个 2 组成的序列。
#
# 比方说，[0,1,2] 和 [0,0,1,1,1,2] 是特殊序列。
# 相反，[2,1,0] ，[1] 和 [0,1,2,0] 就不是特殊序列。
# 给你一个数组 nums （仅 包含整数 0，1 和 2），请你返回 不同特殊子序列的数目 。
# 由于答案可能很大，请你将它对 109 + 7 取余 后返回。
# 一个数组的 子序列 是从原数组中删除零个或者若干个元素后，剩下元素不改变顺序得到的序列。
# 如果两个子序列的 下标集合 不同，那么这两个子序列是 不同的 。
# 示例 1：
# 输入：nums = [0,1,2,2]
# 输出：3
# 解释：特殊子序列为 [0,1,2]，[0,1,2] 和 [0,1,2,2] 。
# 示例 2：
# 输入：nums = [2,2,0,0]
# 输出：0
# 解释：数组 [2,2,0,0] 中没有特殊子序列。
# 示例 3：
# 输入：nums = [0,1,2,0,1,2]
# 输出：7
# 解释：特殊子序列包括：
# - [0,1,2]
# - [0,1,2]
# - [0,1,2,2]
# - [0,1,1,2]
# - [0,0,1,2]
# - [0,1,2]
# - [0,1,2]
# 提示：
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 2
from typing import List

# dp[i][j] 代表前 i 位子序列，j 代表最后一位的取值 {0,1,2}
# dp[i][0] = 2 * dp[i-1][0] + 1
# dp[i][1] = 2 * dp[i-1][1] + dp[i-1][0]
# dp[i][2] = 2 * dp[i-1][2] + dp[i-1][1]
# dp[0~len(nums)][0~2]
# dp[0][0] = 1 if nums[0] == 0 else 0
# dp[0][1] = 1 if nums[0] == 1 else 0
# dp[0][2] = 1 if nums[0] == 2 else 0
class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        dp = [[0,0,0] for i in range(0, len(nums))]
        dp[0][0] = 1 if nums[0] == 0 else 0
        dp[0][1] = 0 if nums[0] == 1 else 0
        dp[0][2] = 0 if nums[0] == 2 else 0
        for i in range(1, len(nums)):
            if nums[i] == 0:
                dp[i][0] = (2 * dp[i-1][0] + 1) % mod
                dp[i][1] = (dp[i-1][1]) % mod
                dp[i][2] = (dp[i-1][2]) % mod
            elif nums[i] == 1:
                dp[i][1] = (2 * dp[i-1][1] + dp[i-1][0]) % mod
                dp[i][0] = (dp[i-1][0]) % mod
                dp[i][2] = (dp[i-1][2]) % mod
            else:
                dp[i][2] = (2 * dp[i-1][2] + dp[i-1][1]) % mod
                dp[i][0] = (dp[i-1][0]) % mod
                dp[i][1] = (dp[i-1][1]) % mod
        return dp[len(nums)-1][2]

    def countSpecialSubsequences2(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        f0, f1, f2 = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                f0 = (2 * f0 + 1) % mod
            elif nums[i] == 1:
                f1 = (2 * f1 + f0) % mod
            else:
                f2 = (2 * f2 + f1) % mod
        return f2

def test():
    s = Solution()
    nums = [0,1,2,2]
    assert s.countSpecialSubsequences(nums) == s.countSpecialSubsequences2(nums)
    nums = [2,2,0,0]
    assert s.countSpecialSubsequences(nums) == s.countSpecialSubsequences2(nums)
    nums = [0,1,2,0,1,2]
    assert s.countSpecialSubsequences(nums) == s.countSpecialSubsequences2(nums)

if __name__ == '__main__':
    test()