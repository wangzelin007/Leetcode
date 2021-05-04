# 一只青蛙想要过河。
# 假定河流被等分为若干个单元格，并且在每一个单元格内都有可能放有一块石子（也有可能没有）。
# 青蛙可以跳上石子，但是不可以跳入水中。
# 给你石子的位置列表 stones（用单元格序号 升序 表示），请判定青蛙能否成功过河（即能否在最后一步跳至最后一块石子上）。
# 开始时，青蛙默认已站在第一块石子上，并可以假定它第一步只能跳跃一个单位（即只能从单元格 1 跳至单元格 2 ）。
# 如果青蛙上一步跳跃了k个单位，那么它接下来的跳跃距离只能选择为k - 1、k或k + 1 个单位。
# 另请注意，青蛙只能向前方（终点的方向）跳跃。
# 示例 1：
# 输入：stones = [0,1,3,5,6,8,12,17]
# 输出：true
# 解释：青蛙可以成功过河，按照如下方案跳跃：跳 1 个单位到第 2 块石子, 然后跳 2 个单位到第 3 块石子, 接着 跳 2 个单位到第 4 块石子, 然后跳 3 个单位到第 6 块石子, 跳 4 个单位到第 7 块石子, 最后，跳 5 个单位到第 8 个石子（即最后一块石子）。
# 示例 2：
# 输入：stones = [0,1,2,3,4,8,9,11]
# 输出：false
# 解释：这是因为第 5 和第 6 个石子之间的间距太大，没有可选的方案供青蛙跳跃过去。
# 提示：
# 2 <= stones.length <= 2000
# 0 <= stones[i] <= 231 - 1
# stones[0] == 0
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/frog-jump
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
from collections import defaultdict
from functools import lru_cache
# 伪代码
# stones 石头列表 index 当前所在位置 k 上一次跳跃的步数
# def helper(stone, index, k):
#     for i in index+1 到 len(stone)-1:
#         gap = stone[i] - stone[index]
#         if gap >= k-1 and gap <= k+1:
#             if helper(stone, i, gap) == True:
#                 return True
#         if gap > k+1: break # 不应该都是break ？ 或者我觉得应该是return False
#         if gap < k-1: continue# 不应该都是break ？ 或者我觉得应该是return False
#     if index == len(stone)-1: return True
#     return False

# 加入记忆化


class Solution:
    # DFS
    def canCross1(self, stones: List[int]) -> bool:
        @lru_cache(None)
        def dfs(pos, step):
            if pos==stones[-1]: return True # 一定要定义结束
            for i in [-1, 0, 1]:
                # set > dict >>> list；set 和 dict 都使用了 hash，list 是可变长度的数组
                if step+i > 0 and pos+step+i in set(stones): # 为了查找更快
                    if dfs(pos+step+i, step+i):
                        return True
            return False
        pos, step = 0, 0
        return dfs(pos, step)

    # 动态规划
    # dp[x] = {y1,y2,y3} x代表当前所在位置，y代表上一次的步数
    def canCross2(self, stones: List[int]) -> bool:
        set_stone = set(stones) # 为了查找更快
        dp = defaultdict(set)
        dp[0] = {0}
        for pos in stones:
            for step in dp[pos]: # 这个其实就是去重的步骤
                for i in [-1, 0, 1]:
                    if step+i > 0 and pos+step+i in set_stone:
                        dp[pos+step+i].add(step+i)
        print(dp)
        return len(dp[stones[-1]]) > 0

if __name__ == '__main__':
    s = Solution()
    stones = [0,1,3,5,6,8,12,17]
    # stones = [0,1,2,3,4,8,9,11]
    print(s.canCross1(stones))
    print(s.canCross2(stones))

