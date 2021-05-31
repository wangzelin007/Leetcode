# 给定一个整数，写一个函数来判断它是否是 4 的幂次方。
# 如果是，返回 true ；否则，返回 false 。
# 整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4x
# 示例 1：
# 输入：n = 16
# 输出：true
# 示例 2：
# 输入：n = 5
# 输出：false
# 示例 3：
# 输入：n = 1
# 输出：true
# 提示：
# -2^31 <= n <= 2^31 - 1
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/power-of-four
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 思路1：二进制情况下，只有1个1 & 位于2的偶数次方上
# 10101010101010101010101010101010 == 0xaaaaaaaa
class Solution1:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n-1)) == 0 and (n & 0xaaaaaaaa) == 0

# 思路2：二进制情况下，只有1个1 & 对3取模余1（2的基数次方对3取模余2
# 4^x % 3 = (3+1)^x % 3 = 1
# ((4^x) * 2) % 3 = 2
class Solution2:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n-1)) == 0 and (n % 3) == 1
