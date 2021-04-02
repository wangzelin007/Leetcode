# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。
#
# 示例：
# 给出如下 3x6 的高度图:
# [
#   [1,4,3,1,3,2],
#   [3,2,1,3,2,4],
#   [2,3,3,2,3,1]
# ]
# 返回 4 。
from heapq import *
import heapq

class Solution:
    def trapRainWater1(self, heightMap):
        """
        水从高出往低处流，某个位置储水量取决于四周最低高度，从最外层向里层包抄，用小顶堆动态找到未访问位置最小的高度
        """
        if not heightMap: return 0
        imax = float('-inf') # inf 正无穷 -inf 负无穷
        ans = 0
        heap = []
        visited = set()
        row = len(heightMap)
        col = len(heightMap[0])
        # 将最外层放入小顶堆
        # 第一行和最后一行
        for j in range(col):
            # 将该位置的高度、横纵坐标插入堆
            heappush(heap, [heightMap[0][j], 0, j])
            heappush(heap, [heightMap[row - 1][j], row - 1, j])
            visited.add((0, j))
            visited.add((row - 1, j))
        # 第一列和最后一列
        for i in range(row): # visited 是set 可以去重，所以不需要去掉头尾列
            heappush(heap, [heightMap[i][0], i, 0])
            heappush(heap, [heightMap[i][col - 1], i, col - 1])
            visited.add((i, 0))
            visited.add((i, col - 1))
        while heap:
            h, i, j = heappop(heap)
            # 之前最低高度的四周已经探索过了，所以要更新为次低高度开始探索
            imax = max(imax, h)
            # 从堆顶元素出发，探索四周储水位置
            for x, y in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                tmp_x = x + i
                tmp_y = y + j
                # 是否到达边界
                if tmp_x < 0 or tmp_y < 0 or tmp_x >= row or tmp_y >= col or (tmp_x, tmp_y) in visited:
                    continue
                visited.add((tmp_x, tmp_y))
                if heightMap[tmp_x][tmp_y] < imax:
                    ans += imax - heightMap[tmp_x][tmp_y]
                heappush(heap, [heightMap[tmp_x][tmp_y], tmp_x, tmp_y])
        return ans

    def trapRainWater2(self, heightMap):
        # 整体是初始化最外围一圈的围栏，模拟围栏外的水不停上涨往里灌的过程
        if not heightMap:
            return 0
        m, n, border = len(heightMap), len(heightMap[0]), []
        for i in range(m):
            border += [(heightMap[i][0], i, 0), (heightMap[i][n-1], i, n-1)]
            heightMap[i][0] = heightMap[i][n-1] = -1  # 标记已访问
        print border
        print heightMap
        for j in range(1, n-1):
            border += [(heightMap[0][j], 0, j), (heightMap[m-1][j], m-1, j)]
            heightMap[0][j] = heightMap[m-1][j] = -1  # 标记已访问
        print border # 高度，横纵坐标
        print heightMap # 外围栏杆都标记为已访问
        heapq.heapify(border)  # 将初始围栏放入以堆存放的优先队列，方便当前围栏最矮处即水的入口
        # inf 正无穷 -inf 负无穷
        res, _h = 0, float('-inf')  # res为答案，_h为当前的水位
        while border:
            h, i, j = heapq.heappop(border)  # 找到围栏的入口
            _h = max(_h, h)  # 如果围栏最矮处变高了水位就涨到该高度
            for _i, _j in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):  # 通过bfs来收缩围栏
                if 0 < _i < m-1 and 0 < _j < n-1 and heightMap[_i][_j] != -1:  # 未访问过，将围栏往内收缩
                    res += max(0, _h-heightMap[_i][_j])  # 如果小于当前围栏则表示该格子可以储水
                    heapq.heappush(border, (heightMap[_i][_j], _i, _j))  # 将其继续加入围栏的优先队列用于继续bfs
                    heightMap[_i][_j] = -1  # 标记已访问
        return res

if __name__ == '__main__':
    s = Solution()
    heightMap = [
        [1,4,3,1,3,2],
        [3,2,1,3,2,4],
        [2,3,3,2,3,1]
        ]
    print(s.trapRainWater1(heightMap))
    print(s.trapRainWater2(heightMap))