# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 给你一个数组 nums ，数组中只包含非负整数。
# 定义 rev(x) 的值为将整数 x 各个数字位反转得到的结果。
# 比方说 rev(123) = 321 ， rev(120) = 21 。
# 我们称满足下面条件的下标对 (i, j) 是 好的 ：
# 0 <= i < j < nums.length
# nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
# 请你返回好下标对的数目。
# 由于结果可能会很大，请将结果对 109 + 7 取余 后返回。
#
# 示例 1：
# 输入：nums = [42,11,1,97]
# 输出：2
# 解释：两个坐标对为：
#  - (0,3)：42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121 。
#  - (1,2)：11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12 。
#
# 示例 2：
# 输入：nums = [13,10,35,24,76]
# 输出：4

class Solution(object):
    def countNicePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = dict()
        res = 0
        for i in nums:
            key = i - int(str(i)[::-1])
            dic[key] = dic.get(key, 0) + 1
        for value in dic.values():
            res += value * (value - 1) // 2
        return res % (10 ** 9 + 7)

if __name__ == '__main__':
    s = Solution()
    nums1 = [42, 11, 1, 97] # 1
    nums2 = [13, 10, 35, 24, 76] # 4
    print(s.countNicePairs(nums1))
    print(s.countNicePairs(nums2))