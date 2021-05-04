from typing import List

class Solution1:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
        dic = {}
        for interval in intervals:
            len = interval[1] - interval[0] + 1
            for i in range(interval[0], interval[1]+1):
                dic[i] = min(dic.get(i,float('inf')), len)
        # print(dic)
        res = []
        for i in queries:
            res.append(dic.get(i, -1))
        # print(res)
        return res

from sortedcontainers import SortedList
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        queries = [[q, i] for i, q in enumerate(queries)]
        ans = [-1] * len(queries)
        s1 = SortedList()
        s2 = SortedList()
        intervals.sort(reverse=1) # [[4, 4], [3, 6], [2, 4], [1, 4]]
        for q, i in sorted(queries, key=lambda p: p[0]):
            while intervals and intervals[-1][0] <= q:
                inte = intervals.pop()
                s1.add(inte[1] - inte[0] + 1)
                s2.add([inte[1], inte[1] - inte[0] + 1])
            while s2 and s2[0][0] < q:
                p = s2.pop(0)
                s1.remove(p[1])
            if s1:
                ans[i] = s1[0]
        return ans


if __name__ == '__main__':
    s = Solution()
    intervals = [[1,4],[2,4],[3,6],[4,4]]; queries = [2,3,4,5] #[3, 3, 1, 4]
    print(s.minInterval(intervals, queries))
    intervals = [[2,3],[2,5],[1,8],[20,25]]; queries = [2,19,5,22] # [2, -1, 4, 6]
    print(s.minInterval(intervals, queries))