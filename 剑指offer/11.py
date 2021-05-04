# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如，数组[3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。
#
# 示例 1：
# 输入：[3,4,5,1,2]
# 输出：1
#
# 示例 2：
# 输入：[2,2,2,0,1]
# 输出：0
class Solution1(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        if len(numbers) == 0: return
        elif len(numbers) == 1: return numbers[0]
        else:
            top1 = numbers.pop()
            while numbers:
                top2 = numbers.pop()
                if top1 < top2:
                    return top1
                else:
                    top1 = top2
            return top1

# 当 nums[m] > nums[j]nums[m]>nums[j] 时： mm 一定在 左排序数组 中，即旋转点 xx 一定在 [m + 1, j][m+1,j] 闭区间内，因此执行 i = m + 1i=m+1；
# 当 nums[m] < nums[j]nums[m]<nums[j] 时： mm 一定在 右排序数组 中，即旋转点 xx 一定在[i, m][i,m] 闭区间内，因此执行 j = mj=m；
# 当 nums[m] = nums[j]nums[m]=nums[j] 时： 无法判断 mm 在哪个排序数组中，即无法判断旋转点 xx 在 [i, m][i,m] 还是 [m + 1, j][m+1,j] 区间中。
# 解决方案： 执行 j = j - 1j=j−1 缩小判断范围。

class Solution(object):
    def minArray(self, numbers):
        i,j = 0,len(numbers)-1
        while i < j:
            m = (i + j) // 2
            if numbers[m] < numbers[j]:
                j = m
            elif numbers[m] > numbers[j]:
                i = m+1
            else:
                j -= 1
        return numbers[i]

class Solution(object):
    def minArray(self, numbers):
        i,j = 0,len(numbers)-1
        while i<j:
            m=(i+j)//2
            if numbers[m] < numbers[j]:
                j=m
            elif numbers[m] > numbers[j]:
                i=m+1
            else:
                return min(numbers[i:j])
        return numbers[i]

if __name__ == '__main__':
    s = Solution()
    print(s.minArray([]))
    print(s.minArray([2]))
    print(s.minArray([2,2,2,0,1]))
    print(s.minArray([3, 4, 5, 1, 2]))

