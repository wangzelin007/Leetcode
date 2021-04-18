# 输入：tasks = [[1,2],[2,4],[3,2],[4,1]]
# 输出：[0,2,3,1]
# 解释：事件按下述流程运行：
# - time = 1 ，任务 0 进入任务队列，可执行任务项 = {0}
# - 同样在 time = 1 ，空闲状态的 CPU 开始执行任务 0 ，可执行任务项 = {}
# - time = 2 ，任务 1 进入任务队列，可执行任务项 = {1}
# - time = 3 ，任务 2 进入任务队列，可执行任务项 = {1, 2}
# - 同样在 time = 3 ，CPU 完成任务 0 并开始执行队列中用时最短的任务 2 ，可执行任务项 = {1}
# - time = 4 ，任务 3 进入任务队列，可执行任务项 = {1, 3}
# - time = 5 ，CPU 完成任务 2 并开始执行队列中用时最短的任务 3 ，可执行任务项 = {1}
# - time = 6 ，CPU 完成任务 3 并开始执行任务 1 ，可执行任务项 = {}
# - time = 10 ，CPU 完成任务 1 并进入空闲状态
import heapq
from typing import List

# 先按照进入时间、用时，下标排序，维护按照用时和下标的小根堆，比当前时间小的入堆，pop堆后更新当前时间
class Solution1:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [[idx, t, d] for idx, (t, d) in enumerate(tasks)]
        tasks.sort(key=lambda x: (x[1], x[2], x[0])) # start long idx
        cur_t = tasks[0][1]
        res = []
        heap = []
        n = len(tasks)
        idx = 0
        while len(res) != n:
            while idx < n and tasks[idx][1] <= cur_t:
                t = tasks[idx]
                heapq.heappush(heap, [t[2], t[0], t[1]])  # d, idx, t
                idx += 1
            if not heap:
                cur_t = tasks[idx][1]
                continue
            cur_task = heapq.heappop(heap)
            res.append(cur_task[1])
            cur_t = max(cur_t, cur_task[2]) + cur_task[0]
        return res

class Solution2:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # [(3, [4, 1]), (2, [3, 2]), (1, [2, 4]), (0, [1, 2])]
        tasks = sorted(enumerate(tasks), key=lambda x: (-x[1][0],-x[1][1],-x[0])) # - 代表降序 start，long ,idx
        ans = []
        pq = []
        time = 0
        while tasks or pq:
            if pq:
                l, idx, t = heapq.heappop(pq)
            else:
                idx, v = tasks.pop()
                t, l = v # time long
            ans.append(idx)
            time = max(t,time) + l # 3 -> 5 -> 6 -> 10
            while tasks and tasks[-1][1][0] <= time: # start <= time
                index, val = tasks.pop()
                ti, le = val
                heapq.heappush(pq, (le, index, ti))
        return ans

from sortedcontainers import SortedList

class Solution3:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        start_time = float('inf')               #开始时间
        for t in tasks:
            start_time = min(start_time, t[0])

        minHeap = []                            #最小堆，以开始时间，花费，idx为顺序排序
        for i in range(len(tasks)):
            begin, cost = tasks[i]
            heapq.heappush(minHeap, (begin, cost, i))

        res = []
        window = SortedList()                   #当前等待队列，CPU可以从中选择

        def dfs(curtime: int, window: SortedList) -> None:

            while minHeap and minHeap[0][0] <= curtime:     #起始时间<=curtime的可以进window
                begin,cost,idx = heapq.heappop(minHeap)
                window.add((cost, idx))

            if len(window) == 0 and len(minHeap) == 0:      #如果window空了，任务处理完了，就结束
                return
            if len(window) == 0:                            #如果window空了，从剩下的挑开始时间最小（早）的，开始
                begin, cost, idx = heapq.heappop(minHeap)
                cur_time = begin
                window.add((cost, idx))

            cost, idx = window.pop(0)       #处理完了这个，弹出window
            res.append(idx)                 #记录好

            dfs(curtime+cost, window)       #继续进行

        dfs(start_time, window)
        return res

if __name__ == '__main__':
    s = Solution3()
    tasks = [[1,2],[2,4],[3,2],[4,1]] # 0,2,3,1
    print(s.getOrder(tasks))
