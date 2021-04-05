# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 小扣当前位于魔塔游戏第一层，共有 N 个房间，编号为 0 ~ N-1。
# 每个房间的补血道具/怪物对于血量影响记于数组 nums，其中正数表示道具补血数值，即血量增加对应数值；
# 负数表示怪物造成伤害值，即血量减少对应数值；0 表示房间对血量无影响。
#
# 小扣初始血量为 1，且无上限。
# 假定小扣原计划按房间编号升序访问所有房间补血/打怪，为保证血量始终为正值，小扣需对房间访问顺序进行调整，
# 每次仅能将一个怪物房间（负数的房间）调整至访问顺序末尾。
# 请返回小扣最少需要调整几次，才能顺利访问所有房间。
# 若调整顺序也无法访问完全部房间，请返回 -1。
#
# 示例 1：
# 输入：nums = [100,100,100,-250,-60,-140,-50,-50,100,150]
# 输出：1
# 解释：初始血量为 1。至少需要将 nums[3] 调整至访问顺序末尾以满足要求。
#
# 示例 2：
# 输入：nums = [-200,-300,400,0]
# 输出：-1
# 解释：调整访问顺序也无法完成全部房间的访问。

# 思路和心得：
#
# 1.贪心
# 当不行了时候，把visit的最小的负数扔到最后
# 2.用堆来实现维护当前最小的负数
# 3.把负数扔到最后，只是眼前避过这一关
# 最后的最后，还是要掉血的

class Solution:
    def magicTower(self, nums):
        n = len(nums)

        cur_sum = 0  # 当前和
        time = 0  # 把负数往后扔的次数
        minSum = 0  # 负数的abs值
        minHeap = []  # 最小堆。每次把最小的负数，扔到后面去

        for i in range(n):
            cur_sum += nums[i]  # 当前和

            if nums[i] < 0:  # 所有的负数，都进堆
                heapq.heappush(minHeap, nums[i])

            if cur_sum < 0:  # 当前卡住了。需要把前面经历过的这些负数中，扔一个最小的到后面
                cur_min = heapq.heappop(minHeap)

                minSum -= cur_min  # 这些扔到后面的，眼前跳过了，在最后还是要掉血
                cur_sum -= cur_min  # 扔掉这个最小的负数。cur_sum会变大
                time += 1  # 记录往后扔的次数

        if cur_sum < minSum:  # 如果正值，不能够把扔到末尾的负值抵消掉
            return -1
        return time
