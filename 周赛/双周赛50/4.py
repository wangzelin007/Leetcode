# todo
# 5720. 使字符串有序的最少操作次数
# 给你一个字符串 s （下标从 0 开始）。
# 你需要对 s 执行以下操作直到它变为一个有序字符串：
# 找到 最大下标 i ，使得 1 <= i < s.length 且 s[i] < s[i - 1] 。
# 找到 最大下标 j ，使得 i <= j < s.length 且对于所有在闭区间 [i, j] 之间的 k 都有 s[k] < s[i - 1] 。
# 交换下标为 i - 1 和 j 处的两个字符。
# 将下标 i 开始的字符串后缀反转。
# 请你返回将字符串变成有序的最少操作次数。
# 由于答案可能会很大，请返回它对 10**9 + 7 取余 的结果。
# 示例 1：
# 输入：s = "cba"
# 输出：5
# 解释：模拟过程如下所示：
# 操作 1：i=2，j=2。交换 s[1] 和 s[2] 得到 s="cab" ，然后反转下标从 2 开始的后缀字符串，得到 s="cab" 。
# 操作 2：i=1，j=2。交换 s[0] 和 s[2] 得到 s="bac" ，然后反转下标从 1 开始的后缀字符串，得到 s="bca" 。
# 操作 3：i=2，j=2。交换 s[1] 和 s[2] 得到 s="bac" ，然后反转下标从 2 开始的后缀字符串，得到 s="bac" 。
# 操作 4：i=1，j=1。交换 s[0] 和 s[1] 得到 s="abc" ，然后反转下标从 1 开始的后缀字符串，得到 s="acb" 。
# 操作 5：i=2，j=2。交换 s[1] 和 s[2] 得到 s="abc" ，然后反转下标从 2 开始的后缀字符串，得到 s="abc" 。
# 示例 2：
# 输入：s = "aabaa"
# 输出：2
# 解释：模拟过程如下所示：
# 操作 1：i=3，j=4。交换 s[2] 和 s[4] 得到 s="aaaab" ，然后反转下标从 3 开始的后缀字符串，得到 s="aaaba" 。
# 操作 2：i=4，j=4。交换 s[3] 和 s[4] 得到 s="aaaab" ，然后反转下标从 4 开始的后缀字符串，得到 s="aaaab" 。
# 示例 3：
# 输入：s = "cdbea"
# 输出：63
# 示例 4：
# 输入：s = "leetcodeleetcodeleetcode"
# 输出：982157772

# 需要一个先验知识，如何计算有重复字母的组合总数。
# 这个可以百度一下，最后的公式是
# 假设有 x个a，y个b，z个c，组合总数为 (x + y + z)! / (x! * y! * z!)

from collections import Counter
import math

class Solution:
    def makeStringSorted(self, s: str) -> int:
        # 求字符串的总共组合数量，用到了那个先验知识
        cnt = Counter(s)
        print(cnt)
        # 和的阶乘
        cur = math.factorial(len(s))
        print(cur)
        for v in cnt.values():
            # 除以阶乘的乘积
            cur //= math.factorial(v)

        res = 0
        for i, v in enumerate(s):
            for ke, va in cnt.items():
                # 当后续某个字符小于当前字符，累加当前的可能性
                # 以上面的描述为例，当b后面出现个a，可以假定当前位置变成a，这种情况下
                # 还剩下 (x - 1)个a，y个b，z个c, 组合总数为 ((x - 1) + y + z)! / ((x - 1)! * y! * z!)
                # 等同为 (x + y + z)! / (x! * y! * z!) * x / (x + y + z)
                # 也就是下面的 cur * va // (len(s) - i)
                if ke < v:
                    res += cur * va // (len(s) - i)
                    print(res)

            # 当字符往后移动时，更新当前的可能的组合数，同时更新Counter
            cur = cur * cnt[v] // (len(s) - i)
            cnt[v] -= 1

        return res % (10 ** 9 + 7)

class Solution2:
    def makeStringSorted(self, s: str) -> int:
        dic = Counter(s)
        MOD = 10 ** 9 + 7
        A = [1]
        for i in range(1, len(s)+1):
            A.append(A[i-1]*i)

        cur = 0
        rest = len(s) - 1
        for c in s:
            lis = sorted(dic.keys())
            idx = lis.index(c)

            div = 1
            # print(dic)
            for value in dic.values():
                div *= A[value]

            dic[c] -= 1
            if dic[c] == 0:
                dic.pop(c)
            num = 0
            #print(lis, c, idx)

            for i in range(idx):
                num += dic[lis[i]]


            tmp = num * A[rest] // div
            #print(len(lis), idx, num, tmp)
            cur = (cur+tmp)%MOD
            rest -= 1

            #for i in range(idx + 1, len(lis)):
            #    tmp = tmp * func()
        return cur % MOD



        # return res % MOD

if __name__ == '__main__':
    a = Solution()
    s = "cba"
    s = "leetcodeleetcodeleetcode"
    s = "aabaa"
    print(a.makeStringSorted(s))