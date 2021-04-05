# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 给你两个正整数数组 nums1 和 nums2 ，数组的长度都是 n 。
# 数组 nums1 和 nums2 的 绝对差值和 定义为所有 |nums1[i] - nums2[i]|（0 <= i < n）的 总和（下标从 0 开始）。
# 你可以选用 nums1 中的 任意一个 元素来替换 nums1 中的 至多 一个元素，以 最小化 绝对差值和。
# 在替换数组 nums1 中最多一个元素 之后 ，返回最小绝对差值和。因为答案可能很大，所以需要对 109 + 7 取余 后返回。
#
# |x| 定义为：
# 如果 x >= 0 ，值为 x ，或者
# 如果 x <= 0 ，值为 -x
#  
# 示例 1：
# 输入：nums1 = [1,7,5], nums2 = [2,3,5]
# 输出：3
# 解释：有两种可能的最优方案：
# - 将第二个元素替换为第一个元素：[1,7,5] => [1,1,5] ，或者
# - 将第二个元素替换为第三个元素：[1,7,5] => [1,5,5]
# 两种方案的绝对差值和都是 |1-2| + (|1-3| 或者 |5-3|) + |5-5| = 3
#
# 示例 2：
# 输入：nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10]
# 输出：0
# 解释：nums1 和 nums2 相等，所以不用替换元素。绝对差值和为 0
#
# 示例 3：
# 输入：nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]
# 输出：20
# 解释：将第一个元素替换为第二个元素：[1,10,4,4,2,7] => [10,10,4,4,2,7]
# 绝对差值和为 |10-9| + |10-3| + |4-5| + |4-1| + |2-7| + |7-4| = 20

# 使用二分查找最接近的树，再比较差值
class Solution(object):
    def minAbsoluteSumDiff(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        def binarySearch(arr, x):
            left, right = 0, len(arr) - 2 # 需要使用mid+1，注意right边界
            while left <= right: #
                mid = left + (right - left) // 2
                #print left,right,mid
                if x - arr[mid] > arr[mid + 1] - x:
                    left = mid + 1
                else:
                    right = mid - 1 #
            return arr[left]

        diff = [abs(nums1[i] - nums2[i]) for i in range(len(nums1))]
        # print 'diff',diff # [1, 4, 0]
        sorted_nums1 = sorted(nums1) # reverse=False 降序 reverse=True 升序
        max_dec, max_dec_i = 0, len(nums1)
        # print 'max_dec',max_dec,'max_dec-i',max_dec_i # 0 3
        for i in range(len(nums1)): # range(3) 0 1 2
            dec = diff[i] - abs(nums2[i] - binarySearch(sorted_nums1, nums2[i]))
            print 'search: ',nums2[i], 'result: ',binarySearch(sorted_nums1, nums2[i])
            # print binarySearch(sorted_nums1,nums2[i]) # 1 1 5
            # print 'dec',dec
            # 1-abs(2-1) = 0
            # 4-abs(3-1) = 2 差距最大
            # 0-abs(5-5) = 0
            if dec > max_dec:
                max_dec, max_dec_i = dec, i # dec=2, i=1, dec 代表差距, i代表位置
        if max_dec > 0:
            diff[max_dec_i] -= max_dec # diff[1] = diff[1] -2 = 4 - 2

        return sum(diff) % (10 ** 9 + 7) # sum([1,2,0])

if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 7, 5]; nums2 = [2, 3, 5] # 3
    nums3 = [2, 4, 6, 8, 10]; nums4 = [2, 4, 6, 8, 10] # 0
    nums5 = [1,10,4,4,2,7]; nums6 = [9,3,5,1,7,4] # 20
    print(s.minAbsoluteSumDiff(nums1, nums2))
    print(s.minAbsoluteSumDiff(nums3, nums4))
    # bs 10
    # bs 2
    # bs 4
    # bs 1
    # bs 7
    # bs 4
    print(s.minAbsoluteSumDiff(nums5, nums6))