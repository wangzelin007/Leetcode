# _*_ coding: utf-8 _*_
# 统计一个数字在排序数组中出现的次数。
# 示例 1:
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: 2
# 示例2:
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: 0
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        return nums.count(target)

# 二分
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            # 右边界
            mid = (i + j) // 2
            if nums[mid] <= target: i = mid + 1
            else: j = mid - 1
        right = i
        if j >= 0 and nums[j] != target: return 0
        i = 0
        while i <= j:
            # 左边界
            mid = (i + j) // 2
            if nums[mid] >= target: j = mid - 1
            else: i = mid + 1
        left = j
        return right - left - 1

# 二分优化
# 搜索 target 右边界 和 target - 1 右边界
class Solution3:
    def search(self, nums: List[int], target: int) -> int:
        def helper(target):
            i , j= 0, len(nums) - 1
            while i <= j:
                m = (i + j) // 2
                if nums[m] <= target: i = m + 1
                else: j = m - 1
            return i
        return helper(target) - helper(target - 1)

# bisect
import bisect
class Solution4:
    def search(self, nums: List[int], target: int) -> int:
        l = bisect.bisect_left(nums, target)
        r = bisect.bisect_right(nums, target)
        return r - l

if __name__ == '__main__':
    s = Solution()
    nums = [5,7,7,8,8,8,10]
    target = 8
    print(s.search(nums, target))