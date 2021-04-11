# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 1. 采购方案
# 小力将 N 个零件的报价存于数组 nums。小力预算为 target，假定小力仅购买两个零件，要求购买零件的花费不超过预算，请问他有多少种采购方案。
# 注意：答案需要以 1e9 + 7 (1000000007) 为底取模，如：计算初始结果为：1000000008，请返回 1
#
# 示例 1：
# 输入：nums = [2,5,3,5], target = 6
# 输出：1
# 解释：预算内仅能购买 nums[0] 与 nums[2]。

# 示例 2：
# 输入：nums = [2,2,1,9], target = 10
# 输出：4

# 解释：符合预算的采购方案如下：
# nums[0] + nums[1] = 4
# nums[0] + nums[2] = 3
# nums[1] + nums[2] = 3
# nums[2] + nums[3] = 10

#双指针
class Solution1(object):
    def purchasePlans(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i, j = 0, len(nums) - 1
        res = 0
        nums.sort()
        while i < j:
            if nums[i] + nums[j] > target:
                j = j - 1
            else:
                res += j - i
                i = i + 1
        return res % (10 ** 9 + 7)

# bisect 二等分
import bisect
# list target low=0 high=len(list)
# L = [1,3,3,6,8,12,15]
# x = 3
# index = bisect.bisect_left(L, x) # 在L中查找x，x存在时返回x左侧的位置, 不存在返回x插入时的位置
# index = bisect.bisect_right(L, x) # 在L中查找x，x存在时返回x右侧的位置, 不存在返回x插入时的位置
# index = bisect.insort_left(L, x) # 将x插入到列表L中，x存在时插入在左侧
# index = bisect.insort_right(L, x) # 将x插入到列表L中，x存在时插入在右侧
# 1
# 3
# [1, 3, 3, 3, 6, 8, 12, 15]
# [1, 3, 3, 3, 3, 6, 8, 12, 15]
# x = 4 bisect_left = biset_right = 3
# 所以要找小于解，用bisect_right好，答案即bisect_right - 1
# print(bisect.bisect_left(L, x, 0))
# print(bisect.bisect_right(L, x, 0))

class Solution2:
    def purchasePlans(self, nums, target):
        nums.sort()
        res = 0
        for i in range(len(nums)):
            if nums[i] > target - nums[i]:
                break
            index = bisect.bisect_right(nums, target - nums[i], i)
            res = (res + index - i - 1) % 1000000007
        return res

# 二分 超时
class Solution(object):
    def purchasePlans(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binarySearch(arr, x):
            print arr
            lo = 0
            hi = len(arr)
            while lo < hi:
                # mid = (lo+hi)//2
                mid = lo + (hi-lo)//2
                if x < arr[mid]: hi = mid
                else: lo = mid+1
            return lo
            # hi = len(arr) - 1
            # while lo <= hi:
                # mid = start + (end - start) // 2
                # if arr[mid] <= x:
                #     start = mid + 1
                # else:
                #     end = mid - 1
            # return start

        res = 0
        nums.sort()

        for i in range(len(nums)):
            if target - nums[i] >= nums[i]:
                res += binarySearch(nums[i+1:], target - nums[i]) % (10 ** 9 + 7)
            else:
                break
        return res

if __name__ == '__main__':
    s = Solution()
    # nums = [2, 5, 3, 5]; target = 6 # 1
    nums = [2, 2, 1, 9, 10, 11, 12]; target = 10 # 4
    print(s.purchasePlans(nums, target))