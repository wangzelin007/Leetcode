# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
# 你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。
#
# 示例 1：
# 输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# 输出：[1,2,2,3,5,6]
#
# 示例 2：
# 输入：nums1 = [1], m = 1, nums2 = [], n = 0
# 输出：[1]

# 排序法
class Solution1(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()

# 双指标法
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i, j = m-1, n-1
        target = m + n -1
        while i >= 0 or j >= 0:
            if i == -1:
                nums1[target] = nums2[j]
                j -= 1
            elif j == -1:
                nums1[target] = nums1[i]
                i -= 1
            elif nums1[i] < nums2[j]:
                nums1[target] = nums2[j]
                j -= 1
            else:
                nums1[target] = nums1[i]
                i -= 1
            target -= 1


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]; m = 3; nums2 = [2, 5, 6]; n = 3
    # nums1 = [1]; m = 1; nums2 = []; n = 0
    s.merge(nums1, m, nums2, n)
    print nums1


