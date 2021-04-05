# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 某实验室计算机待处理任务以 [start,end,period] 格式记于二维数组 tasks，
# 表示完成该任务的时间范围为起始时间 start 至结束时间 end 之间，需要计算机投入 period 的时长，注意：
#
# period 可为不连续时间
# 首尾时间均包含在内
# 处于开机状态的计算机可同时处理任意多个任务，请返回电脑最少开机多久，可处理完所有任务。
#
# 示例 1：
# 输入：tasks = [[1,3,2],[2,5,3],[5,6,2]]
# 输出：4
# 解释：
# tasks[0] 选择时间点 2、3；
# tasks[1] 选择时间点 2、3、5；
# tasks[2] 选择时间点 5、6；
# 因此计算机仅需在时间点 2、3、5、6 四个时刻保持开机即可完成任务。
#
# 示例 2：
# 输入：tasks = [[2,3,1],[5,5,1],[5,6,2]]
# 输出：3
# 解释：
# tasks[0] 选择时间点 2 或 3；
# tasks[1] 选择时间点 5；
# tasks[2] 选择时间点 5、6；
# 因此计算机仅需在时间点 2、5、6 或 3、5、6 三个时刻保持开机即可完成任务。

# 解题思路
# 首先，对于这一类问题，一般来说使用左开右闭区间[L,R)[L,R)是更优的。因此，我们在离散化时间戳时，将所有区间都按照[L,R)[L,R)的方式来进行处理。
#
# 显然，我们应当尽可能晚地执行任务，因为这样的话，当次执行有可能服务于更多的区间。
#
# 这里我们引入【槽位】的概念。所谓【槽位】，指的是一个任务当前能够空闲的最大时长。比如一个[1,6)[1,6)的任务，需要投入2的时长，那么它就有3个槽位，因为我们可以在[4,6)[4,6)进行执行，从而空出[1,4)[1,4)。
#
# 在离散化之后，我们逐段进行处理。显然，在考虑一段区间时，我们应当以当前剩余槽位最少的任务为准来进行安排。如果当前剩余槽位最少的为1个槽位，那么这个区间的开头最多空出1个位置，而后面的位置都得执行任务。
#
# 首先，我们将结束时间在当前时间之前的任务出队。
# 我们将当前时刻开始的任务入队。这里，我们在计算出该任务的槽位后，需要加上一个修正项extra，后面会说到。
# 我们考虑当前槽位最少的那个任务。以它为准进行任务执行之后，如果当前区间空了kk个位置，那么当前队列中的所有任务的剩余槽位都会减少kk。显然我们无法对队列中的每个元素进行操作。但我们可以反其道而行之，给之后入队的元素加上k。这里，我们把之后入队的元素需要累加的修正量记录在变量extra中。
# 时间复杂度\mathcal{O}(M\log M+N\log N)O(MlogM+NlogN)，其中MM是不同的时间戳的数目，NN是任务的数目。
#
# 作者：lucifer1004
# 链接：https://leetcode-cn.com/problems/t3fKg1/solution/you-xian-dui-lie-tan-xin-rust-by-lucifer-4spv/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from heapq import heapify, heappush, heappop


class Solution:
    def processTasks(self, tasks: List[List[int]]) -> int:
        n = len(tasks)
        ts = set()
        for s, e, _ in tasks:
            ts.add(s)
            ts.add(e + 1)

        vt = sorted(list(ts))
        mp = dict()
        for i, t in enumerate(vt):
            mp[t] = i

        m = len(vt)
        starts = [[] for _ in range(m)]
        for i, task in enumerate(tasks):
            starts[mp[task[0]]].append(i)

        ans = 0
        extra = 0  # 关键变量，用于修正优先队列内的数值
        pq = []
        heapify(pq)

        for i in range(m - 1):
            while pq and tasks[pq[0][1]][1] < vt[i]:
                heappop(pq)

            for u in starts[i]:
                heappush(pq, (extra + tasks[u][1] - vt[i] + 1 - tasks[u][2], u))

            current_seg = vt[i + 1] - vt[i]

            if pq:
                # 减去extra得到实际的空余槽位数目。
                min_slots = pq[0][0] - extra
                slots_to_del = current_seg

                # 如果空余槽位最少的那个任务的空余槽位小于当前区间的长度，则当前区间需要安排任务。
                if min_slots < current_seg:
                    delta = current_seg - min_slots
                    ans += delta
                    slots_to_del -= delta

                # 需要减少当前队列内的任务的空余槽位，这里显然不能逐个修改，所以变为增加之后入队的任务的数值。
                extra += slots_to_del

        return ans
