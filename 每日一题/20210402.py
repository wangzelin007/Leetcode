# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 给定一个直方图(也称柱状图)，假设有人从上面源源不断地倒水，最后直方图能存多少水量?直方图的宽度为 1。
#
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的直方图，在这种情况下，可以接 6 个单位的水（蓝色部分表示水）。
#        |
#    |   || |
# _|_||_||||||
# 示例:
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6

# O(N) O(N)
# 动态规划 求交集
# sum(min(左边最大存水，右边最大存水）- 当前高度)
class Solution1:
    def trap(self, height):
        if not height:
            return 0

        n = len(height)
        leftMax = [height[0]] + [0] * (n - 1)
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
        print leftMax

        rightMax = [0] * (n - 1) + [height[n - 1]]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        print rightMax

        ans = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
        return ans

# O(N) O(N)
# 单调栈
# 小于前项入栈，大于计算长度并出栈。
class Solution2:
    def trap(self, height):
        ans = 0
        stack = list()
        n = len(height)

        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                currWidth = i - left - 1
                currHeight = min(height[left], height[i]) - height[top]
                ans += currWidth * currHeight
            stack.append(i)

        return ans

# O(N) O(1)
# 双指针相遇法
# 用leftMax 表示左指针的最大高度
# 用rightMax 表示右指针的最大高度
# min(leftMax,rightMax)-height
class Solution3:
    def trap(self, height):
        ans = 0
        left, right = 0, len(height) - 1
        leftMax = rightMax = 0

        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if height[left] < height[right]:
                ans += leftMax - height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1

        return ans

# 总体积 - 柱子体积 = 水体积
# 总体积按行求和
#
class Solution4:
    def trap(self, height):
        Sum = sum(height) # 得到柱子的体积
        size = len(height)
        left, right = 0, size - 1 # 双指针初始化
        volume, high = 0, 1 # 总体积和高度初始化
        while (left <= right):
            while (left <= right and height[left] < high):
                left += 1
            while (left <= right and height[right] < high):
                right -= 1
            volume += right - left + 1 # 每一层的容量都加起来
            high += 1 # 高度加一
        return volume - Sum # 总体积减去柱子体积，即雨水总量

if __name__ == '__main__':
    s = Solution()
    s.trap([0,1,0,2,1,0,1,3,2,1,2,1])