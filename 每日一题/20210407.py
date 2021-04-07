# _*_ coding: utf-8 _*_
# 33. 搜索旋转排序数组
# 整数数组 nums 按升序排列，数组中的值 互不相同 。
# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。
# 例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为[4,5,6,7,0,1,2] 。
# 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回-1。

# 思路：只要是有序的数组，即时多次旋转也可以使用二分查找，因为部分有序。
# 难点：做好边界情况的处理。

# 1. nums[mid] = target: return mid
# 2. nums[0] <= nums[mid]:
#    a. nums[0] <= target < nums[mid]: right=mid-1
#    b. else: target 在右半部分，left=mid+1
# 3.nums[0] > nums[mid]:
#    a. nums[mid] < target <= nums[len(nums)-1]: left=mid+1
#    b. else: target 在左半部分，right=mid-1
# 是否可以将0换为left，len(nums)-1换为right 可以！！！
class Solution1(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target: return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]: right = mid - 1
                else: left = mid + 1
            else:
                if nums[mid] < target <= nums[right]: left = mid + 1
                else: right = mid - 1
        return -1

# 81. 搜索旋转排序数组 II
# 已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。
# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转 ，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。
# 例如， [0,1,2,4,4,4,5,6,6,7] 在下标 5 处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。
# 给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值是否存在于数组中。
# 如果 nums 中存在这个目标值 target ，则返回 true ，否则返回 false 。
# 1. nums[mid] = target: return True
# 2. nums[left] = nums[mid] and nums[right] = nums[mid]: left-1 and right-1
# 3. nums[left] <= nums[mid]:
#     a. nums[left] <= target < nums[mid]: right=mid-1
#     b. else: target在右半部分，left=mid+1
# 4. nums[left] > nums[mid]:
#     a. nums[mid] < target <= nums[right]: left=mid+1
#     b. else: target在左半部分，right=mid-1
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # 特例
        if not nums: return False
        if len(nums) == 1: return nums[0] == target
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2 # (l + r) // 2 也可以
            if nums[mid] == target: return True
            if nums[left] == nums[mid] == nums[right]: left += 1; right -= 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]: right = mid - 1
                else: left = mid + 1
            else:
                if nums[mid] < target <= nums[right]: left = mid + 1
                else: right = mid - 1
        return False

if __name__ == '__main__':
    s = Solution()
    nums = [1,1,1,1,1,1,1,1,1,13,1,1,1,1,1,1,1,1,1,1,1,1]
    target = 13
    print(s.search(nums, target))

# 面试题 10.03. 搜索旋转数组 todo
# 搜索旋转数组。给定一个排序后的数组，包含n个整数，但这个数组已被旋转过很多次了，次数不详。
# 请编写代码找出数组中的某个元素，假设数组元素原先是按升序排列的。
# 若有多个相同元素，返回索引值最小的一个。
#
# 示例1:
# 输入: arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 5
# 输出: 8（元素5在该数组中的索引）
#
# 示例2:
# 输入：arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 11
# 输出：-1 （没有找到）
