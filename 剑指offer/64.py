# 求 1+2+...+n ，要求不能使用乘除法、
# for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
# 示例 1：
# 输入: n = 3
# 输出: 6
# 示例 2：
# 输入: n = 9
# 输出: 45
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/qiu-12n-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 使用 and or 代替循环或者迭代的终止
class Solution:
    def __init__(self):
        self.res = 0

    def sumNums1(self, n: int) -> int:
        n > 1 and self.sumNums1(n-1)
        self.res += n
        return self.res

    def sumNums2(self, n: int) -> int:
        n < 1 or self.sumNums2(n-1)
        self.res += n
        return self.res

    # 如果 and 结果为真，返回最后一个表达式的值。
    # 如果 or 结果为真，返回第一个表达式的值。
    def sumNums(self, n: int) -> int:
        return n and (n + self.sumNums(n-1))

if __name__ == '__main__':
    s = Solution()
    assert s.sumNums(10) == 55