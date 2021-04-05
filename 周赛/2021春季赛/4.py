# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 某解密游戏中，有一个 N*M 的迷宫，迷宫地形会随时间变化而改变，迷宫出口一直位于 (n-1,m-1) 位置。
# 迷宫变化规律记录于 maze 中，maze[i] 表示 i 时刻迷宫的地形状态，"." 表示可通行空地，"#" 表示陷阱。
#
# 地形图初始状态记作 maze[0]，此时小力位于起点 (0,0)。
# 此后每一时刻可选择往上、下、左、右其一方向走一步，或者停留在原地。
#
# 小力背包有以下两个魔法卷轴（卷轴使用一次后消失）：
# 临时消除术：将指定位置在下一个时刻变为空地；
# 永久消除术：将指定位置永久变为空地。
# 请判断在迷宫变化结束前（含最后时刻），小力能否在不经过任意陷阱的情况下到达迷宫出口呢？
# 注意： 输入数据保证起点和终点在所有时刻均为空地。
#
# 示例 1：
# 输入：maze = [[".#.","#.."],["...",".#."],[".##",".#."],["..#",".#."]]
# 输出：true
#
# 示例 2：
# 输入：maze = [[".#.","..."],["...","..."]]
# 输出：false
# 解释：由于时间不够，小力无法到达终点逃出迷宫。
#
# 示例 3：
# 输入：maze = [["...","...","..."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."]]
# 输出：false
# 解释：由于道路不通，小力无法到达终点逃出迷宫。

# 解题思路
# dfs，需要记录的有花销时间，当前坐标，卷轴使用状态。
#
# 如果碰到一个障碍，可以选择使用 卷轴1 或者 卷轴2，
#
# 使用完卷轴后，可以上、下、左、右、不动。
#
# 对于卷轴1，如果不动的话，那么当前位置就永远不会恢复。只要移动了，那么卷轴1就使用完毕。
#
# 对于卷轴2，使用后，这个位置永远变为空地。
#
# 剪枝1：时间花完；
#
# 剪枝2：走完剩下的路需要的最小时间 < 剩余时间，那么此路不通。
#
# 其他的就是套模板了。
#
# 注：用bfs也可以的，只需要将栈改成队列即可。
#
# 作者：moguqicha
# 链接：https://leetcode-cn.com/problems/Db3wC1/solution/dfsbfstong-li-by-moguqicha-vb0k/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def escapeMaze(self, maze: List[List[str]]) -> bool:
        time = len(maze)
        X = len(maze[0])
        Y = len(maze[0][0])
        stk = []
        stk.append((0, 0, 0, 1, 1))  #  时刻、坐标x、坐标y、卷轴1、卷轴2
        seen = set()
        while stk:
            cur = stk.pop()
            if cur in seen:
                continue
            seen.add(cur)
            x, y, t, roll1, roll2 = cur
            if t == time:  # 时间花完，
                continue
            if Y-y-1 + X-x-1 > time-t-1:  # 走完剩下的路需要的最小时间 < 剩余时间，那么此路不通
                continue
            if x == X-1 and y == Y-1:
                return True
            if maze[t][x][y] == '#': # 使用一个卷轴
                if roll1: # 使用roll1
                    stk.append((x, y, t+1, 2, roll2)) # 原地不动
                    for dx, dy in (-1, 0), (0, -1), (1, 0), (0, 1):
                        curx, cury = x + dx, y + dy
                        if 0 <= curx < X and 0 <= cury < Y:
                            stk.append((curx, cury, t+1, 0, roll2))
                if  roll2 and roll1 != 2: # 使用卷轴2，如果使用卷轴1并且没有动，就不能使用卷轴2
                    for dx, dy in (-1, 0), (0, -1), (1, 0), (0, 1):
                        curx, cury = x + dx, y + dy
                        if 0 <= curx < X and 0 <= cury < Y:
                            stk.append((curx, cury, t+1, roll1, 0))
                continue
            if roll1 == 2:
                stk.append((x, y, t+1, 2, roll2)) # 原地不动
                for dx, dy in (-1, 0), (0, -1), (1, 0), (0, 1):
                    curx, cury = x + dx, y + dy
                    if 0 <= curx < X and 0 <= cury < Y:
                        stk.append((curx, cury, t+1, 0, roll2))
            else:
                stk.append((x, y, t+1, roll1, roll2)) # 原地不动
                for dx, dy in (-1, 0), (0, -1), (1, 0), (0, 1):
                    curx, cury = x + dx, y + dy
                    if 0 <= curx < X and 0 <= cury < Y:
                        stk.append((curx, cury, t+1, roll1, roll2))
        return False
