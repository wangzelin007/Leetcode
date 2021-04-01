# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 通常，正整数 n 的阶乘是所有小于或等于 n 的正整数的乘积。例如，factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1。
# 相反，我们设计了一个笨阶乘 clumsy：在整数的递减序列中，我们以一个固定顺序的操作符序列来依次替换原有的乘法操作符：乘法(*)，除法(/)，加法(+)和减法(-)。
# 例如，clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1。然而，这些运算仍然使用通常的算术运算顺序：我们在任何加、减步骤之前执行所有的乘法和除法步骤，并且按从左到右处理乘法和除法步骤。
# 另外，我们使用的除法是地板除法（floor division），所以 10 * 9 / 8 等于 11。这保证结果是一个整数。
# 实现上面定义的笨函数：给定一个整数 N，它返回 N 的笨阶乘。
class Solution1(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        sum = ""
        opr = ['*', '/', '+', '-']
        j = 0
        for i in range(N, 0, -1):
            sum = sum + '%s%s' %(i,opr[j]) if i-1 else sum + '%s' % i
            j = 0 if j == 3 else j+1
        return eval(sum)

# 15*14/13+12-11*10/9+8-7*6/5+4-3*2/1
# [0, 1, 2, 6, 7] N<=4
class Solution2(object):
    def clumsy(self, N):
        para = [0, 1, 2, 6, 7]
        if N<=4:
            res = para[N]
        else:
            res = N*(N-1)/(N-2)+(N-3)
            N -= 4
            while N > 4:
                res = res - N*(N-1)/(N-2) + (N-3)
                N -= 4
            res = res - para[N]
        return res

# 1.除了4*3/2=6 3*2/1=6 以外 N * N-1 / N -2 = N + 1
# 4位4*3/2+1 6 大于4位 5*4/3+2-1 6
class Solution3(object):
    def clumsy(self, N):
        para = [0, 1, 2, 6, 7]
        if N<=4:
            res = para[N]
        else:
            res = N+1 + (N-3)
            N -= 4
            while N > 4:
                res = res - 4
                N -= 4
            res = res - para[N]
        return res

# 如果没有规律呢？如何用栈实现
class Solution4(object):
    def clumsy(self, N):
        opt = ['*', '/', '+', '-']
        j = 0
        opr = '+'
        stack = []
        for i in range(N,0,-1):
            if opr == '+':
                stack.append(i)
            elif opr == '-':
                stack.append(-i)
            elif opr == '*':
                top = stack.pop()
                stack.append(top*i)
            elif opr == '/':
                top = stack.pop()
                if top < 0:
                    stack.append(-(abs(top)/i))
                else:
                    stack.append(top/i)
            opr = opt[j]
            j = 0 if j==3 else j+1
        return sum(stack)

# 满足任意规律的炒作符
class Solution(object):
    def clumsy(self, N):
        opt = ['*', '/', '+', '-']
        j = 0
        opr = '+'
        stack = []
        flag = True
        top = 0
        for i in range(N,0,-1):
            if opr == '+':
                if not flag:
                    flag = not flag
                    stack.append(top)
                    top = 0
                stack.append(i)
            elif opr == '-':
                if not flag:
                    flag = not flag
                    stack.append(top)
                    top = 0
                stack.append(-i)
            elif opr == '*':
                if flag:
                    top = stack.pop()
                    flag = not flag
                top = top*i
            elif opr == '/':
                if flag:
                    top = stack.pop()
                    flag = not flag
                if top < 0:
                    top = -(abs(top)/i)
                else:
                    top = top/i
            opr = opt[j]
            j = 0 if j==3 else j+1
        return sum(stack)+top

if __name__ == '__main__':
    s = Solution()
    print(s.clumsy(1)) #1
    print(s.clumsy(2)) #2
    print(s.clumsy(3)) #6
    print(s.clumsy(4)) #7
    print(s.clumsy(5)) #5*4/3+2-1 7
    print(s.clumsy(6)) #6*5/4+3-2*1 8
    print(s.clumsy(7)) #7*6/5+4-3*2/1 6