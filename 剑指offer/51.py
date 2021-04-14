# _*_ coding: utf-8 _*_
# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
# 输入一个数组，求出这个数组中的逆序对的总数。
#
# 示例 1:
# 输入: [7,5,6,4]
# 输出: 5
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 7,5 7,6 7,4 5,4 6,4 3+1+1
# 肯定超时
class Solution1(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, 1
        res = 0
        while i < len(nums):
            while j < len(nums):
                if nums[i] > nums[j]:
                    res += 1
                j += 1
            i += 1
            j = i + 1
        return res

# 归并排序
# 分治是为了两两交换，所以可以统计次数
class Solution(object):
    def reversePairs(self, nums):
        def divideSort(nums):
            if len(nums) <= 1: return nums
            mid = len(nums) // 2
            left = divideSort(nums[:mid])
            right = divideSort(nums[mid:])
            lIndex, rIndex = 0, 0
            result = []
            while lIndex < len(left) and rIndex < len(right):
                if left[lIndex] <= right[rIndex]:
                    result.append(left[lIndex])
                    lIndex += 1
                else:
                    result.append(right[rIndex])
                    self.res += len(left) - lIndex
                    rIndex += 1
            result += left[lIndex:]
            result += right[rIndex:]
            return result
        self.res = 0
        divideSort(nums)
        return self.res

class Solution3:
    def reversePairs(self, nums):
        def merge_sort(l, r):
            # 终止条件
            if l >= r: return 0
            # 递归划分
            m = (l + r) // 2
            res = merge_sort(l, m) + merge_sort(m + 1, r) # 闭包
            # 合并阶段
            i, j = l, m + 1
            tmp[l:r + 1] = nums[l:r + 1]
            for k in range(l, r + 1):
                if i == m + 1:
                    nums[k] = tmp[j]
                    j += 1
                elif j == r + 1 or tmp[i] <= tmp[j]:
                    nums[k] = tmp[i]
                    i += 1
                else:
                    nums[k] = tmp[j]
                    j += 1
                    res += m - i + 1 # 统计逆序对
            return res # 闭包

        tmp = [0] * len(nums)
        return merge_sort(0, len(nums) - 1) # 闭包

if __name__ == '__main__':
    s = Solution()
    nums = [7,5,6,4]
    print(s.reversePairs(nums))



