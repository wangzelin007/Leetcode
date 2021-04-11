# _*_ coding: utf-8 _*_
# 已知函数 signFunc(x) 将会根据 x 的正负返回特定值：
# 如果 x 是正数，返回 1 。
# 如果 x 是负数，返回 -1 。
# 如果 x 是等于 0 ，返回 0 。
# 给你一个整数数组 nums 。令 product 为数组 nums 中所有元素值的乘积。

class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 1
        for i in nums:
            if i == 0: return 0
            elif i < 0: res = -res
            else: continue
        return res