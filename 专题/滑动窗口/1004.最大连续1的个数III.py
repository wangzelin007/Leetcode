# _*_ coding: utf-8 _*_
# 给定一个由若干 0 和 1 组成的数组A，我们最多可以将k个值从 0 变成 1 。
# 返回仅包含 1 的最长（连续）子数组的长度。
#
# 示例 1：
# 输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# 输出：6
# 解释：
# [1,1,1,0,0,1,1,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 6。
#
# 示例 2：
# 输入：A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# 输出：10
# 解释：
# [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 10。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/max-consecutive-ones-iii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 滑动窗口模板(虫取法)
# def findSubArray(nums):
#     N = len(nums) # 数组/字符串长度
#     left, right = 0, 0 # 双指针，表示当前遍历的区间[left, right]，闭区间
#     sums = 0 # 用于统计 子数组/子区间 是否有效，根据题目可能会改成求和/计数
#     res = 0 # 保存最大的满足题目要求的 子数组/子串 长度
#     while right < N: # 当右边的指针没有搜索到 数组/字符串 的结尾
#         sums += nums[right] # 增加当前右边指针的数字/字符的求和/计数
#         while 区间[left, right]不符合题意：# 此时需要一直移动左指针，直至找到一个符合题意的区间
#         sums -= nums[left] # 移动左指针前需要从counter中减少left位置字符的求和/计数
#         left += 1 # 真正的移动左指针，注意不能跟上面一行代码写反
#     # 到 while 结束时，我们找到了一个符合题意要求的 子数组/子串
#     res = max(res, right - left + 1) # 需要更新结果
#     right += 1 # 移动右指针，去探索新的区间
# return res

# 代码思路：
# 使用 left 和 right 两个指针，分别指向滑动窗口的左右边界。
# right 主动右移：right 指针每次移动一步。当 A[right] 为 0，说明滑动窗口内增加了一个 0；
# left 被动右移：判断此时窗口内 0 的个数，如果超过了 K，则 left 指针被迫右移，直至窗口内的 0 的个数小于等于 K 为止。
# 滑动窗口长度的最大值就是所求。
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 左开右闭
        n = len(nums)
        res = 0
        left = right = 0
        zeros = 0
        while right < n:
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            res = max(res, right-left+1)
            right += 1
        return res