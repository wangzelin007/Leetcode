# You are given an m x n binary matrix grid.
# An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.

# Input: grid = [
#     [0,0,1,0,0,0,0,1,0,0,0,0,0],
#     [0,0,0,0,0,0,0,1,1,1,0,0,0],
#     [0,1,1,0,1,0,0,0,0,0,0,0,0],
#     [0,1,0,0,1,1,0,0,1,0,1,0,0],
#     [0,1,0,0,1,1,0,0,1,1,1,0,0],
#     [0,0,0,0,0,0,0,0,0,0,1,0,0],
#     [0,0,0,0,0,0,0,1,1,1,0,0,0],
#     [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.


from typing import List

# BFS
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        max_area = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    tmp_max = 0
                    tmp_max += 1
                    grid[i][j] = 0
                    neighbors = [(i, j)]
                    while neighbors:
                        i, j = neighbors.pop()
                        for x, y in directions:
                            if 0 <= i+x < m and 0 <= j+y < n and grid[i+x][j+y] == 1:
                                tmp_max += 1
                                grid[i+x][j+y] = 0
                                neighbors.append((i+x, j+y))
                    max_area = max(max_area, tmp_max)
        return max_area


# DFS
class Solution1:
    def __init__(self):
        self.max_area = 0
        self.visited = set()
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid
        for i in range(self.m):
            for j in range(self.n):
                self.tmp_max = 0
                self.floodfill_dfs(i, j)
                self.max_area = max(self.max_area, self.tmp_max)
        return self.max_area

    def floodfill_dfs(self, x, y):
        if not self._is_valid(x, y):
            return
        self.visited.add((x, y))
        self.tmp_max += 1
        for k in range(4):
            self.floodfill_dfs(x + self.dx[k], y + self.dy[k])

    def _is_valid(self, x, y):
        if x < 0 or x >= self.m or y < 0 or y >= self.n:
            return False
        if self.grid[x][y] == 0 or (x, y) in self.visited:
            return False
        return True


# UnionFind
class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.roots = [-1] * (m * n)
        self.rank = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.roots[i * n + j] = i * n + j
                    self.count += 1
                    self.rank[i * n + j] += 1

    def find(self, i):
        if self.roots[i] != i:
            self.roots[i] = self.find(self.roots[i])
        return self.roots[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.roots[rooty] = rootx
                self.rank[rootx] += self.rank[rooty]
            elif self.rank[rootx] < self.rank[rooty]:
                self.roots[rootx] = rooty
                self.rank[rooty] += self.rank[rootx]
            else:
                self.roots[rooty] = rootx
                self.rank[rootx] += self.rank[rooty]
            self.count -= 1


class Solution2:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        uf = UnionFind(grid)
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                for d in directions:
                    x, y = i + d[0], j + d[1]
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        uf.union(i * n + j, x * n + y)
        return max(uf.rank)

