# _*_ coding: utf-8 _*_
# 给定一个二进制数组， 计算其中最大连续 1 的个数。
#
# 示例：
# 输入：[1,1,0,1,1,1]
# 输出：3
# 解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/max-consecutive-ones
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        c = 0
        for i in nums:
            if i == 1:
                c += 1
            else:
                res.append(c)
                c = 0
        res.append(c)
        return max(res)

# 大佬做法,1的位置-0的位置
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        index=-1
        res = 0
        for i, num in enumerate(nums):
            if num == 0:
                index = i
            else:
                res = max(res, i-index)
        return res