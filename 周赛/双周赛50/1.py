# 5717. 最少操作使数组递增
# 给你一个整数数组 nums （下标从 0 开始）。
# 每一次操作中，你可以选择数组中一个元素，并将它增加 1 。
# 比方说，如果 nums = [1,2,3] ，你可以选择增加 nums[1] 得到 nums = [1,3,3] 。
# 请你返回使 nums 严格递增 的 最少 操作次数。
# 我们称数组 nums 是 严格递增的 ，当它满足对于所有的 0 <= i < nums.length - 1 都有 nums[i] < nums[i+1] 。
# 一个长度为 1 的数组是严格递增的一种特殊情况。
# 示例 1：
# 输入：nums = [1,1,1]
# 输出：3
# 解释：你可以进行如下操作：
# 1) 增加 nums[2] ，数组变为 [1,1,2] 。
# 2) 增加 nums[1] ，数组变为 [1,2,2] 。
# 3) 增加 nums[2] ，数组变为 [1,2,3] 。
# 示例 2：
# 输入：nums = [1,5,2,4,1]
# 输出：14
# 示例 3：
# 输入：nums = [8]
# 输出：0
class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1: return 0
        res = 0
        pre = nums[0]
        for i in range(1,n):
            if nums[i] <= pre:
                res += pre + 1 - nums[i]
                pre = pre + 1
            else:
                pre = nums[i]
        return res

from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        for num in nums:
            # max(1,nums[0])
            cur = max(cur+1, num)
            res += cur - num
        return res

if __name__ == '__main__':
    s = Solution()
    nums = [1,5,2,4,1]
    assert s.minOperations(nums) == 14
    nums = [8]
    assert s.minOperations(nums) == 0
    nums = [1,1,1]
    assert s.minOperations(nums) == 3