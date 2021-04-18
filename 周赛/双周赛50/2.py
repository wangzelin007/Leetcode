# 5718. 统计一个圆中点的数目
# 给你一个数组 points ，其中 points[i] = [xi, yi] ，表示第 i 个点在二维平面上的坐标。
# 多个点可能会有 相同 的坐标。
# 同时给你一个数组 queries ，其中 queries[j] = [xj, yj, rj] ，表示一个圆心在 (xj, yj) 且半径为 rj 的圆。
# 对于每一个查询 queries[j] ，计算在第 j 个圆 内 点的数目。
# 如果一个点在圆的 边界上 ，我们同样认为它在圆 内 。
# 请你返回一个数组 answer ，其中 answer[j]是第 j 个查询的答案。
# 输入：points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]
# 输出：[3,2,2]
# 输入：points = [[1,1],[2,2],[3,3],[4,4],[5,5]], queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]
# 输出：[2,3,2,4]

class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # xi <= xj + r or yi <= yj + r
        # (xi-xj)**2 + (yi-yj)**2 <= r**2
        res = [0] * len(queries)
        i = 0
        for xj, yj, r in queries:
            pts = filter(lambda a: a[0]<= xj+r or a[1] <= yj+r, points)
            for xi, yi in pts:
                if (xi-xj)**2 + (yi-yj)**2 <= r**2:
                    res[i] += 1
            i += 1
        return res

from typing import List

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        def dist(x1, y1, x2, y2):
            return (x1-x2)**2+(y1-y2)**2
        res = [0] * len(queries)
        i = 0
        for x1, y1, r1 in queries:
            for x2, y2 in points:
                # print(x1, y1, x2, y2, dist(x1, y1, x2, y2))
                if dist(x1, y1, x2, y2) <= r1 ** 2:
                    res[i] += 1
            i += 1
        return res

if __name__ == '__main__':
    s = Solution()
    points, queries = [[1,1],[2,2],[3,3],[4,4],[5,5]], [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]
    print(s.countPoints(points, queries))
    points, queries = [[1,3],[3,3],[5,3],[2,2]], [[2,3,1],[4,3,1],[1,1,2]]
    print(s.countPoints(points, queries))