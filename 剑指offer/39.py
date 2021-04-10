# _*_ coding: utf-8 _*_
# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
# 示例1:
# 输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
# 输出: 2
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution1(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        dic = {}
        for i in nums:
            dic[i] = dic.get(i,0) + 1
            if dic[i] > l / 2: return i

# 先排序，找中间数
class Solution2(object):
    def majorityElement(self, nums):
        nums.sort()
        mid = len(nums) / 2
        return nums[mid]

# 摩尔投票法: 适用于超过一半的情况
# 最差联合起来，也剩一个。如果其他人内斗，剩下的众数更多
class Solution3(object):
    def majorityElement(self, nums):
        votes = 0
        for num in nums:
            if votes == 0: x = num
            votes += 1 if num == x else -1
        return x

# 如果没有众数，加上验证手段
class Solution(object):
    def majorityElement(self, nums):
        votes = count = 0
        for num in nums:
            if votes == 0: x = num
            votes += 1 if num == x else -1
        print x
        for num in nums:
            count += 1 if num == x else 0
        return x if count > len(nums) / 2 else False


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,2,2,2,5,4,2]
    print(s.majorityElement(nums))
    nums = [1,2,3,2,2,2,5,4]
    print(s.majorityElement(nums))