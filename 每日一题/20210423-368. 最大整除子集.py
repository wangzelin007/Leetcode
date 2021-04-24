# 368. 最大整除子集
# 给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i], answer[j]) 都应当满足：
# answer[i] % answer[j] == 0 ，或
# answer[j] % answer[i] == 0
# 如果存在多个有效解子集，返回其中任何一个均可。
# 示例 1：
# 输入：nums = [1,2,3]
# 输出：[1,2]
# 解释：[1,3] 也会被视为正确答案。
# 示例 2：
# 输入：nums = [1,2,4,8]
# 输出：[1,2,4,8]
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/largest-divisible-subset
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# dp 思路：排序后，对每个一个比自己小的num做%法，求出所有num 对应的 dp[i]
# 取最大的一个dp
from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dp = [[num] for num in nums]
        for i in range(1,n):
            for j in range(i-1,-1,-1):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j]+[nums[i]], key=len)
        return max(dp, key=len)

if __name__ == '__main__':
    s = Solution()
    print(s.largestDivisibleSubset([1,2,3]))
    assert s.largestDivisibleSubset([1,2,4,8]) == [1,2,4,8]
    print(s.largestDivisibleSubset([3,4,16,8]))
