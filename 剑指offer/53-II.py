# 一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
# 在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
# 示例 1:
# 输入: [0,1,3]
# 输出: 2
# 示例2:
# 输入: [0,1,2,3,4,5,6,7,9]
# 输出: 8
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 0,1,2,3,4,5,6,7,10 = 38 +2 10
# 0,1,2,3,4,5,6,7,8 = (0+8)*9/2=36
# 0,2,3,4,5,6,7,8,9 = 44 +8 9
# 只可能是最后一个数字
from typing import List
class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        tmp = set(i for i in range(n))
        return int(list(tmp - set(nums))[0])

# 有序数组的搜索 首选二分！
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r) // 2
            if nums[m] == m:
                l = m + 1
            else:
                r = m -1
        return l

if __name__ == '__main__':
    s = Solution()
    nums = [0,1,2,3,4,5,6,7,10]
    print(s.missingNumber(nums))
