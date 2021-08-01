# 给你一个整数 n 。
# 如果 n 恰好有三个正除数 ，返回 true ；否则，返回 false 。
# 如果存在整数 k ，满足 n = k * m ，那么整数 m 就是 n 的一个 除数 。
# 示例 1：
# 输入：n = 2
# 输出：false
# 解释：2 只有两个除数：1 和 2 。
# 示例 2：
# 输入：n = 4
# 输出：true
# 解释：4 有三个除数：1、2 和 4 。
class Solution:
    def isThree(self, n: int) -> bool:
        if n <= 3: return False
        return self.find_divisor(n)

    def find_divisor(self, n):
        cnt = 2
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                cnt += 1
        return cnt == 3

def test():
    n = 12
    s = Solution()
    assert s.isThree(n) == False

if __name__ == '__main__':
    test()