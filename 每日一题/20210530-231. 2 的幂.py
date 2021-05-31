# 给你一个整数 n，请你判断该整数是否是 2 的幂次方。
# 如果是，返回 true ；否则，返回 false 。
# 如果存在一个整数 x 使得n == 2x ，则认为 n 是 2 的幂次方。
# 示例 1：
# 输入：n = 1
# 输出：true
# 解释：2^0 = 1
# 示例 2：
# 输入：n = 16
# 输出：true
# 解释：2^4 = 16
# 示例 3：
# 输入：n = 3
# 输出：false
# 示例 4：
# 输入：n = 4
# 输出：true
# 示例 5：
# 输入：n = 5
# 输出：false
# 提示：
# -231 <= n <= 231 - 1
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/power-of-two
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and bin(n).count('1') == 1

class Solution2:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0

class Solution3:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & -n) == n

if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfTwo(4))
    print(s.isPowerOfTwo(3))
    print(s.isPowerOfTwo(-16))