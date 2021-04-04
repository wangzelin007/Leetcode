# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 给你用户在 LeetCode 的操作日志，和一个整数 k 。
# 日志用一个二维整数数组 logs 表示，其中每个 logs[i] = [IDi, timei] 表示 ID 为 IDi 的用户在 timei 分钟时执行了某个操作。
#
# 多个用户 可以同时执行操作，单个用户可以在同一分钟内执行 多个操作 。
# 指定用户的 用户活跃分钟数（user active minutes，UAM） 定义为用户对 LeetCode 执行操作的 唯一分钟数 。
# 即使一分钟内执行多个操作，也只能按一分钟计数。
# 请你统计用户活跃分钟数的分布情况，统计结果是一个长度为 k 且 下标从 1 开始计数 的数组 answer ，对于每个 j（1 <= j <= k），answer[j] 表示 用户活跃分钟数 等于 j 的用户数。
# 返回上面描述的答案数组 answer 。
#
# 示例 1：
# 输入：logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5
# 输出：[0,2,0,0,0]
# 解释：
# ID=0 的用户执行操作的分钟分别是：5 、2 和 5 。因此，该用户的用户活跃分钟数为 2（分钟 5 只计数一次）
# ID=1 的用户执行操作的分钟分别是：2 和 3 。因此，该用户的用户活跃分钟数为 2
# 2 个用户的用户活跃分钟数都是 2 ，answer[2] 为 2 ，其余 answer[j] 的值都是 0
#
# 示例 2：
# 输入：logs = [[1,1],[2,2],[2,3]], k = 4
# 输出：[1,1,0,0]
# 解释：
# ID=1 的用户仅在分钟 1 执行单个操作。因此，该用户的用户活跃分钟数为 1
# ID=2 的用户执行操作的分钟分别是：2 和 3 。因此，该用户的用户活跃分钟数为 2
# 1 个用户的用户活跃分钟数是 1 ，1 个用户的用户活跃分钟数是 2
# 因此，answer[1] = 1 ，answer[2] = 1 ，其余的值都是 0
class Solution1(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        dic1 = {}
        dic2 = {}
        ref = [0] * k
        for i in logs:
            id, logTimes = i[0], i[1]
            if id not in dic1: dic1[id] = set()
            dic1[id].add(logTimes)
        for k, v in dic1.items():
            dic1[k] = len(dic1[k])
        for k,v in dic1.items():
            dic2[v] = dic2.get(v,0) + 1
        for k,v in dic2.items():
            ref[k-1] = v
        return ref

class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        dic = {}
        ref = [0] * k
        for i in logs:
            id, logTimes = i[0], i[1]
            if id not in dic: dic[id] = set()
            dic[id].add(logTimes)
        for v in dic.values():
            count = len(v)
            ref[count-1] += 1
        return ref

if __name__ == '__main__':
    logs = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
    k = 5
    s = Solution()
    print(s.findingUsersActiveMinutes(logs, k))