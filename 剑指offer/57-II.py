# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
# 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
# 示例 1：
# 输入：target = 9
# 输出：[[2,3,4],[4,5]]
# 示例 2：
# 输入：target = 15
# 输出：[[1,2,3,4,5],[4,5,6],[7,8]]
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

# 双指针
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i, j, s, res = 1, 2, 3, []
        while i < j:
            if s == target:
                res.append(list(range(i,j+1)))
            if s < target:
                j += 1
                s += j
            else:
                s -= i
                i += 1
        return res

if __name__ == '__main__':
    s = Solution()
    target = 15
    print(s.findContinuousSequence(target))

# 数学法
# https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/jian-zhi-offer-57-ii-he-wei-s-de-lian-xu-t85z/
class Solution2:
    def findContinuousSequence(self, target: int):
        # 一元二次方程求根公式: 韦达定理
        # t = (i+j)*(j-i+1)/2
        # t = (j**2 + j - i**2 + i)/2
        # j**2 + j - (2t + i**2 - i) = 0
        # j = -1 +/- (1 + 4 * (2*t + i * i -i)) ** 0.5 / 2
        i, j, res = 1, 2, []
        while i < j:
            j = (-1 + (1 + 4 * (2 * target + i * i - i)) ** 0.5) / 2
            if i < j and j == int(j):
                res.append(list(range(i, int(j) + 1)))
            i += 1
        return res
