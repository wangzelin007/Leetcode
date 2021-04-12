# _*_ coding: utf-8 _*_
# 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。
# 求所有子数组的和的最大值。
# 要求时间复杂度为O(n)。
#
# 示例1:
# 输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释:连续子数组[4,-1,2,1] 的和最大，为6。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 动态规划
# 定义dp[i] 代表以nums[i]结尾的子数组的和的最大值。
# 则 dp[i-1] 代表以nums[i-1]结尾的子数组的和的最大值。
# 1. 如果dp[i-1] < 0,贡献为负 dp[i] = nums[i] 必须包含，即连续。
# 2. 如果dp[i-1] > 0, dp[i] = dp[i-1] + nums[i]

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            if dp[i-1] > 0:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)

# 大佬写法
class Solution(object):
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            nums[i] += max(nums[i-1], 0)
        return max(nums)