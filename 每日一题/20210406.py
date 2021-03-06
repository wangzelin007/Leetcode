# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 最多出现两次 ，返回删除后数组的新长度。
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
#
# 说明：
# 为什么返回数值是整数，但输出的答案是数组呢？
# 请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
# 你可以想象内部操作如下:
# nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
# int len = removeDuplicates(nums);
# 在函数里修改输入数组对于调用者是可见的。
# 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }

# 单指标隔位比较
def removeDuplicates(nums):
    if len(nums) <= 2:
        return

    cur = 2
    while cur < len(nums):
        if nums[cur] == nums[cur - 2]:
            nums.pop(cur)
            print nums
        else:
            cur += 1

    return

if __name__ == '__main__':
    nums = [0,1,1,1,1,1,2,2,2,3,3,3,4,4]
    removeDuplicates(nums)