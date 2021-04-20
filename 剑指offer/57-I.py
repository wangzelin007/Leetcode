# 输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。
# 如果有多对数字的和等于s，则输出任意一对即可。
# 示例 1：
# 输入：nums = [2,7,11,15], target = 9
# 输出：[2,7] 或者 [7,2]
# 示例 2：
# 输入：nums = [10,26,30,31,47,60], target = 40
# 输出：[10,30] 或者 [30,10]
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
import bisect

class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, n = 0, len(nums)-1
        while True:
            x = target - nums[i]
            idx = bisect.bisect_left(nums, x, lo=i+1)
            if idx <=n and nums[idx] == x:
                return [nums[i], nums[idx]]
            i += 1
        return -1

# 对撞双指针
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums)-1
        while i < j:
            sum = nums[i] + nums[j]
            if sum < target:
                i += 1
            elif sum > target:
                j -= 1
            else:
                return [nums[i], nums[j]]

if __name__ == '__main__':
    s = Solution()
    nums = [2,7,11,15]; target = 9
    assert s.twoSum(nums, target) == [2, 7]
    nums = [10,26,30,31,47,60]; target = 40
    assert s.twoSum(nums, target) == [10, 30]
    # nums = [1,2,3,6,50,60,70,80]; target = 6
    # print(s.twoSum(nums, target))
    # assert s.twoSum(nums, target) == -1
    nums = [14,15,16,22,53,60]; target = 76
    assert s.twoSum(nums, target) == [16, 60]