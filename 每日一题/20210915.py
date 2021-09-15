# 162.
# A peak element is an element that is strictly greater than its neighbors.
# Given an integer array nums, find a peak element, and return its index.
# If the array contains multiple peaks, return the index to any of the peaks.
# You may imagine that nums[-1] = nums[n] = -∞.
# You must write an algorithm that runs in O(log n) time.
#
# Example 1:
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
#
# Constraints:
# 1 <= nums.length <= 1000
# -231 <= nums[i] <= 231 - 1
# nums[i] != nums[i + 1] for all valid i.
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        # You may imagine that nums[-1] = nums[n] = -∞.
        def get(i: int) -> int:
            if i == -1 or i == n:
                return float('-inf')
            return nums[i]

        l, r, ans = 0, n - 1, -1
        while l <= r:
            m = l + (r - l) // 2
            if get(m - 1) < get(m) > get(m + 1):
                ans = m
                break
            elif get(m) < get(m + 1):
                l = m + 1
            else: # 隐含了 nums[m - 1] > nums[m]
                r = m - 1
        return ans

def test():
    s = Solution()
    assert s.findPeakElement([1,2,3,1]) == 2
    assert s.findPeakElement([1,2,1,3,5,6,4]) == 5

if __name__ == '__main__':
    test()