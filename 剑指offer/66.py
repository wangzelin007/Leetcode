# 给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，
# 其中B[i] 的值是数组 A 中除了下标 i 以外的元素的积, 即B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。
# 不能使用除法。
# 示例:
# 输入: [1,2,3,4,5]
# 输出: [120,60,40,30,24]
# 提示：
# 所有元素乘积之和不会溢出 32 位整数
# a.length <= 100000
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
from functools import reduce

# 两个dp，由一条分割线分为下三角和上三角
# a 0 1 2 3 4
# 0 1 2 3 4 5
# 1 1 1 3 4 5
# 2 1 2 1 4 5
# 3 1 2 3 1 5
# 4 1 2 3 4 1
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        dp = [1] * len(a); tmp = 1
        for i in range(1, len(a)):
            dp[i] = dp[i-1] * a[i-1] # 下三角
        for j in range(len(a)-2, -1, -1):
            tmp *= a[j+1]
            dp[j] *= tmp
        return dp

# 我想的是 *（1/x) 也可以的，可能不是考点？
class Solution2:
    def constructArr(self, a: List[int]) -> List[int]:
        if not a: return []
        res = [reduce(lambda x, y: x * y, a[1:])]
        print(res)
        for i in range(1, len(a)):
            if a[i] == 0: res.append(reduce(lambda x, y: x*y, a[:i]+a[i+1:]))
            else: res.append(int(res[-1]*a[i-1]*(a[i]**-1)))
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.constructArr([1,2,3,4,5]))
    print(s.constructArr([1, 2, 0, 4, 5]))
    print(s.constructArr([]))
    print(s.constructArr([7, 2, 2, 4, 2, 1, 8, 8, 9, 6, 8, 9, 6, 3, 2, 1]))
