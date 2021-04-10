# _*_ coding: utf-8 _*_
# 263.丑数 简单
# 给你一个整数 n ，请你判断 n 是否为 丑数 。
# 如果是，返回 true ；否则，返回 false 。
# 丑数 就是只包含质因数2、3 和/或5的正整数。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/ugly-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution1(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1: return True
        if n < 1: return False
        while n > 1:
            if not n % 2: n /= 2
            elif not n % 3: n /= 3
            elif not n % 5: n /= 5
            else: return False
        return True

class Solution2(object):
    def isUgly(self, n):
        if n < 1: return False
        factors = [2,3,5]
        for i in factors:
            while not n % i:
                n /= i
        return n == 1

# 递归
class Solution(object):
    def isUgly(self, n):
        if n < 1: return False
        if n == 1: return True
        if n % 2 == 0: return self.isUgly(n/2)
        if n % 3 == 0: return self.isUgly(n/3)
        if n % 5 == 0: return self.isUgly(n/5)
        return False

if __name__ == '__main__':
    s = Solution()
    n1 = 0
    n2 = 1
    n3 = 8
    n4 = 14
    print(s.isUgly(n1))
    print(s.isUgly(n2))
    print(s.isUgly(n3))
    print(s.isUgly(n4))