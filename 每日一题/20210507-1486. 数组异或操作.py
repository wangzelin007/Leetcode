# 给你两个整数，n 和 start 。
# 数组 nums 定义为：nums[i] = start + 2*i（下标从 0 开始）且 n == nums.length 。
# 请返回 nums 中所有元素按位异或（XOR）后得到的结果。
# 示例 1：
# 输入：n = 5, start = 0
# 输出：8
# 解释：数组 nums 为 [0, 2, 4, 6, 8]，其中 (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8 。
# "^" 为按位异或 XOR 运算符。
# 示例 2：
# 输入：n = 4, start = 3
# 输出：8
# 解释：数组 nums 为 [3, 5, 7, 9]，其中 (3 ^ 5 ^ 7 ^ 9) = 8.
# 示例 3：
# 输入：n = 1, start = 7
# 输出：7
# 示例 4：
# 输入：n = 10, start = 5
# 输出：2
# 提示：
# 1 <= n <= 1000
# 0 <= start <= 1000
# n == nums.length
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/xor-operation-in-an-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 模拟
class Solution1:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        for i in range(n):
            ans ^= start+2*i
        print(ans)
        return ans

# 数学 异或运算满足的性质！
# x⊕x=0；
# x⊕y=y⊕x（交换律）；
# (x⊕y)⊕z=x⊕(y⊕z)（结合律）；
# x⊕y⊕y=x（自反性）；
# 4i⊕(4i+1)⊕(4i+2)⊕(4i+3)=0。
# 在本题中，我们需要计算 start⊕(start+2i)⊕(start+4i)⊕⋯⊕(start+2(n−1))。
# 观察公式可以知道，这些数的奇偶性质相同，因此它们的二进制表示中的最低位或者均为 1，或者均为 0。
# 于是我们可以把参与运算的数的二进制位的最低位提取出来单独处理。当且仅当 start 为奇数，且 n 也为奇数时，结果的二进制位的最低位才为 1。
# 此时我们可以将公式转化为 (s⊕(s+1)⊕(s+2)⊕⋯⊕(s+n−1))×2+e，其中 s=start/2，e 表示运算结果的最低位。
# 即我们单独处理最低位，而舍去最低位后的数列恰成为一串连续的整数。
# 这样我们可以描述一个函数 sumXor(x)，表示 0⊕1⊕2⊕⋯⊕x。
# 利用异或运算的性质 5，我们可以将计算该函数的复杂度降低到 O(1)，因为以 4i 为开头的连续四个整数异或的结果为 0，所以 sumXor(x) 可以被表示为：
# sumXor(x):
# x,                   x=4k,k∈Z
# (x−1)⊕x,             x=4k+1,k∈Z
# (x−2)⊕(x−1)⊕x,       x=4k+2,k∈Z
# (x−3)⊕(x−2)⊕(x−1)⊕x, x=4k+3,k∈Z
# 简化:
# x,                   x=4k,k∈Z
# 1,                   x=4k+1,k∈Z # 因为 1 ⊕ 偶数 = 偶数+1 = x+1
# x+1,                 x=4k+2,k∈Z # 因为 x+1 ⊕ x+1 = 0
# 0,                   x=4k+3,k∈Z
# (s)^(s+1)^(s+2)^(s+3)^...^(s+(n-1)) = (1^2^3^...^(s-1)) ^ (1^2^3^...^(s+n-1)) = sumXor(s-1) ^ sumXor(s+n-1)
# 3^4^5^6^7^8^9 = (1^2)^(1^2^3^4^5^6^7^8^9)
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        def sumXor(x: int) -> int:
            if x % 4 == 0: return x
            elif x % 4 == 1: return 1
            elif x % 4 == 2: return x+1
            else: return 0
        s, e = start>>1, n&start&1 # s = start(偶)/2; e = 运算结果的最低位,因为&1代表只关注最后一位
        ret = sumXor(s-1) ^ sumXor(s+n-1) # 如上所示
        # n = 1, start = 7
        # n = 10, start = 5
        print(ret<<1 | e) # ret * 2 + e

if __name__ == '__main__':
    s = Solution()
    n = 5; start = 0
    s.xorOperation(n, start)
    n = 4; start = 3
    s.xorOperation(n, start)
    n = 1; start = 7
    s.xorOperation(n, start)
    n = 10; start = 5
    s.xorOperation(n, start)