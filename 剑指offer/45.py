# _*_ coding: utf-8 _*_
# 输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
#
# 示例 1:
# 输入: [10,2]
# 输出: "102"
# 示例 2:
# 输入: [3,30,34,5,9]
# 输出: "3033459"
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 快排演进
class Solution(object):
    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def quickSort(arr, l, r):
            i, j = l, r
            if l >= r: return
            while i < j:
                # 字符串的比较就是逐个字符比较
                while i < j and arr[j] + arr[l] >= arr[l] + arr[j]:
                    j -= 1
                while i < j and arr[i] + arr[l] <= arr[l] + arr[i]:
                    i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[i], arr[l] = arr[l], arr[i]
            quickSort(arr, l, i - 1)
            quickSort(arr, i + 1, j)

        nums = [str(i) for i in nums]
        quickSort(nums, 0, len(nums)-1)
        return "".join(nums)

from functools import cmp_to_key
# cmp 默认升序
class Solution(object):
    def minNumber(self, nums):
        def sort_rule(x, y):
            a, b = x + y, y + x
            if a > b: return 1
            elif a < b: return -1
            else: return 0

        strs = [str(i) for i in nums]
        strs.sort(key=cmp_to_key(sort_rule))
        return ''.join(strs)


