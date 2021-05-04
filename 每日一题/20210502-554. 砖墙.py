# 你的面前有一堵矩形的、由 n 行砖块组成的砖墙。
# 这些砖块高度相同（也就是一个单位高）但是宽度不同。
# 每一行砖块的宽度之和应该相等。
# 你现在要画一条 自顶向下 的、穿过 最少 砖块的垂线。
# 如果你画的线只是从砖块的边缘经过，就不算穿过这块砖。
# 你不能沿着墙的两个垂直边缘之一画线，这样显然是没有穿过一块砖的。
# 给你一个二维数组 wall ，该数组包含这堵墙的相关信息。
# 其中，wall[i] 是一个代表从左至右每块砖的宽度的数组。
# 你需要找出怎样画才能使这条线 穿过的砖块数量最少 ，并且返回 穿过的砖块数量 。
# 示例 1：
# 输入：wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
# 输出：2
# 示例 2：
# 输入：wall = [[1],[1],[1]]
# 输出：3
# 提示：
# n == wall.length
# 1 <= n <= 104
# 1 <= wall[i].length <= 104
# 1 <= sum(wall[i].length) <= 2 * 104
# 对于每一行 i ，sum(wall[i]) 应当是相同的
# 1 <= wall[i][j] <= 231 - 1
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/brick-wall
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
from collections import defaultdict
# 前缀和
class Solution1:
    def leastBricks(self, wall: List[List[int]]) -> int:
        def cumsum(l):
            res=[l[0]]
            for i in range(1,len(l)):
                res.append(res[-1]+l[i])
            return res
        # 对于每一行 求前 k 块砖的长度 不包括总长度
        cum_mat = [cumsum(l) for l in wall]
        print(cum_mat)
        # 求前缀和出现次数最多的数字 就是应该选择的宽度
        # （1）defaultdict(int)：默认值为 0
        # （2）defaultdict(float)：默认值为 0.0
        # （3）defaultdict(str)：默认值为 ''
        freq = defaultdict(int)
        for cum in cum_mat:
            #注意哦 这里不要取到最后一个前缀和 因为题目说了不能再墙的最右侧边缘划分
            for num in cum[0:len(cum)-1]:
                freq[num]+=1
        # 如果freq为空,说明每一行都只有一个元素 比如[[1],[1],[1]],只能从中间截取
        print(freq)
        keep_max = max(freq.values()) if freq else 0
        return len(wall)-keep_max

class Solution2:
    def leastBricks(self, wall: List[List[int]]) -> int:
        hashmap = {0: 0}
        for row in wall:
            tmp = 0
            for col in row[:-1]:
                tmp += col
                hashmap[tmp] = hashmap.get(tmp, 0) + 1
        return len(wall) - max(hashmap.values())

if __name__ == '__main__':
    s = Solution2()
    wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
    print(s.leastBricks(wall))