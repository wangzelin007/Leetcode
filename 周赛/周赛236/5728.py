# _*_ coding: utf-8 _*_
# 给你一个长度为n的3跑道道路，它总共包含n + 1个点，编号为0到n。
# 一只青蛙从0号点第二条跑道出发，它想要跳到点n处。然而道路上可能有一些障碍。
# 给你一个长度为 n + 1的数组obstacles，其中obstacles[i]（取值范围从 0 到 3）表示在点 i处的obstacles[i]跑道上有一个障碍。
# 如果obstacles[i] == 0，那么点i处没有障碍。任何一个点的三条跑道中最多有一个障碍。
#
# 比方说，如果obstacles[2] == 1，那么说明在点 2 处跑道 1 有障碍。
# 这只青蛙从点 i跳到点 i + 1且跑道不变的前提是点 i + 1的同一跑道上没有障碍。
# 为了躲避障碍，这只青蛙也可以在同一个点处侧跳到另外一条跑道（这两条跑道可以不相邻），但前提是跳过去的跑道该点处没有障碍。
# 比方说，这只青蛙可以从点 3 处的跑道 3 跳到点 3 处的跑道 1 。
# 这只青蛙从点 0 处跑道 2出发，并想到达点 n处的 任一跑道 ，请你返回 最少侧跳次数。
# 注意：点 0处和点 n处的任一跑道都不会有障碍。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-sideway-jumps
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 贪心
class Solution1(object):
    def minSideJumps(self, obstacles):
        n = len(obstacles)
        curr = 2
        lines = {1, 2, 3}
        ans = 0
        for i in range(n-1): # 最后一步必为0
            # an obstacle in front of
            if obstacles[i+1] == curr:
                # places can jump to (即 lines - obs[i] - obs[i+1])
                new_lines = lines - {curr, obstacles[i]}
                if len(new_lines) == 1:
                    curr = new_lines.pop() # 更新当前 且集合只能pop()
                else:
                    # jump to the place where we can go as far as we can 贪心
                    max_index = -1
                    for j in new_lines:
                        try:
                            # list value start stop 返回范围内第一次出现的index值
                            index = obstacles.index(j, i+1, n)
                            # index = list.index(obstacles, j, i+1, n)
                            if index > max_index:
                                max_index = index
                                curr = j # 更新当前
                        except: # index 不存在时会raise ValueError
                            return ans + 1 # 找不到index时，index=无限大，只需要加一次，即跳到这个路径下，直接能到终点
                ans += 1 # obs[i+1] == curr
        return ans

# 动态规划
# dp[i][j]表示到达第i处第j跑道的最少跳跃次数,一共六种情况
# 最后一步不换*3
# 跑道dp[i][0] = dp[i-1][0]
# 跑道dp[i][1] = dp[i-1][1]
# 跑道dp[i][2] = dp[i-1][2]
# 最后一步换*3
# 跑道dp[i][0] = min(dp[i][1], dp[i][2]) + 1
# 跑道dp[i][1] = min(dp[i][0], dp[i][2]) + 1
# 跑道dp[i][2] = min(dp[i][0], dp[i][1]) + 1
# 换与不换比较
# dp[i][0] = min(dp[i][0], min(dp[i][1], dp[i][2]) + 1)
# dp[i][1] = min(dp[i][1], min(dp[i][0], dp[i][2]) + 1)
# dp[i][2] = min(dp[i][2], min(dp[i][0], dp[i][1]) + 1)
# 三个出口的比较
# min(dp[n-1][0], dp[n-1][1], dp[n-1][2])
class Solution(object):
    def minSideJumps(self, obstacles):
        n = len(obstacles)
        # 未知要用最大值 float('inf'） 用0，结果就是0了
        dp = [[float('inf')] * 3 for _ in range(n)]
        dp[0][0] = 1
        dp[0][1] = 0
        dp[0][2] = 1
        for i in range(1, n):
            # 倒数第二步不跳
            if obstacles[i] != 1: dp[i][0] = dp[i-1][0]
            if obstacles[i] != 2: dp[i][1] = dp[i-1][1]
            if obstacles[i] != 3: dp[i][2] = dp[i-1][2]
            # 取倒数第二步不跳和跳的最小值
            if obstacles[i] != 1: dp[i][0] = min(dp[i][0], min(dp[i][1], dp[i][2]) + 1)
            if obstacles[i] != 2: dp[i][1] = min(dp[i][1], min(dp[i][0], dp[i][2]) + 1)
            if obstacles[i] != 3: dp[i][2] = min(dp[i][2], min(dp[i][0], dp[i][1]) + 1)
        return min(dp[n-1][0], dp[n-1][1], dp[n-1][2]) # 取三个出口的最小值

if __name__ == '__main__':
    s = Solution()
    obstacles1 = [0,1,2,3,0]
    obstacles2 = [0,1,1,3,3,0]
    obstacles3 = [0,2,1,0,3,0]
    obstacles4 = [0,2,0,3,1]
    obstacles5 = [0,2,2,1,0,3,0,3,0,1,0]
    print(s.minSideJumps(obstacles1)) # 2
    print(s.minSideJumps(obstacles2)) # 0
    print(s.minSideJumps(obstacles3)) # 2
    print(s.minSideJumps(obstacles4)) # 2
    print(s.minSideJumps(obstacles5)) # 2

