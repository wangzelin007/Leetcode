# 给定一个非负整数c，你要判断是否存在两个整数 a 和 b，使得a^2 + b^2 = c 。
# 示例 1：
# 输入：c = 5
# 输出：true
# 解释：1 * 1 + 2 * 2 = 5
# 示例 2：
# 输入：c = 3
# 输出：false
# 示例 3：
# 输入：c = 4
# 输出：true
# 示例 4：
# 输入：c = 2
# 输出：true
# 示例 5：
# 输入：c = 1
# 输出：true
# 提示：
# 0 <= c <= 231 - 1
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sum-of-square-numbers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
#          r
#     0  1  2  3  4  5
#   0 0  1  4  9  16 25
#   1 1  2  5  10 17 26
# l 2 4  5  8  13 20 29
#   3 9  10 13 18 25 34
#   4 16 17 20 25 32 41
#   5 25 26 29 34 41 50
# 矩阵思维
# 时间复杂度 O(c**0.5) 空间复杂度：O(1)
class Solution1:
    def judgeSquareSum(self, c: int) -> bool:
        # 这里必须int, 否则不是整数！！！
        l, r = 0, int(c**0.5)
        while l<=r:
            sumOf = l*l+r*r
            if sumOf == c: return True
            elif sumOf < c: l += 1
            else: r -= 1
        return False

# 为什么我觉得 sqrt 是笨办法呢？
# 因为我还不会算复杂度
# 其实和 Solution1 一样
# 时间复杂度 O(c**0.5) 空间复杂度：O(1)。
class Solution2:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        while i**2 <= c:
            j = (c - i**2) ** 0.5
            if j == int(j): return True
            i += 1
        return False

# 费马平方和定理告诉我们：
# 一个非负整数 c 如果能够表示为两个整数的平方和，
# 当且仅当 c 的所有形如 4k + 3 的质因子的幂均为偶数。
# todo
class Solution3:
    def judgeSquareSum(self, c: int) -> bool:
        pass

if __name__ == '__main__':
    # s = Solution1()
    s = Solution2()
    print(s.judgeSquareSum(31))