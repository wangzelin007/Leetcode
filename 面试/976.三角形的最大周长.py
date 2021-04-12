# _*_ coding: utf-8 _*_
# 给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。
# 如果不能形成任何面积不为零的三角形，返回0。
#
# 示例 1：
# 输入：[2,1,2]
# 输出：5
# 示例 2：
# 输入：[1,2,1]
# 输出：0
# 示例 3：
# 输入：[3,2,3,4]
# 输出：10
# 示例 4：
# 输入：[3,6,2,3]
# 输出：8
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/largest-perimeter-triangle
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 只要有最大最小想着贪心算法！
# 贪心+排序
# 为什么 i >= 2,因为取前两个
class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        nums.sort()
        n = len(nums)
        for i in range(n-1,1,-1):
            if nums[i-1] + nums[i-2] > nums[i]:
                return nums[i] + nums[i-1] + nums[i-2]
        return res