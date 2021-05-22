# 给你一个整数数组 arr 。
# 现需要从数组中取三个下标 i、j 和 k ，其中 (0 <= i < j <= k < arr.length) 。
# a 和 b 定义如下：
# a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
# b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
# 注意：^ 表示 按位异或 操作。
# 请返回能够令 a == b 成立的三元组 (i, j , k) 的数目。
# 示例 1：
# 输入：arr = [2,3,1,6,7]
# 输出：4
# 解释：满足题意的三元组分别是 (0,1,2), (0,2,2), (2,3,4) 以及 (2,4,4)
# 示例 2：
# 输入：arr = [1,1,1,1,1]
# 输出：10
# 示例 3：
# 输入：arr = [2,3]
# 输出：0
# 示例 4：
# 输入：arr = [1,3,5,7,9]
# 输出：3
# 示例 5：
# 输入：arr = [7,11,12,9,5,2,7,17,22]
# 输出：8
# 提示：
# 1 <= arr.length <= 300
# 1 <= arr[i] <= 10^8
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
# b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
# Si = 0 if i == 0 else arr0⊕arr1⊕...⊕arri-1
# a = Si⊕Sj
# b = Sj⊕Sk+1
# Si = Sk+1

# 三重循环
class Solution1:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        s = [0]
        for val in arr:
            s.append(s[-1] ^ val)

        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j, n):
                    if s[i] == s[k+1]:
                        ans += 1
        return ans

# 双重循环
# 当等式 Si=Sk+1成立时，[i+1,k] 的范围内的任意 j 都是符合要求的，对应的三元组个数为 k−i。因此我们只需枚举下标 i 和 k。
class Solution2:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        s = [0]
        for val in arr:
            s.append(s[-1] ^ val)

        ans = 0
        for i in range(n):
            for k in (i+1, n):
                if s[i] == s[k+1]:
                    ans += 1
        return ans

# 一重循环
# 对于下标k，若下标 i=i1,i2,...,im 时均满足Si=Sk+1, 根据方法二，这些i对答案的贡献为：
# k-i1 + k-i2 + ... + k-im = mk -(i1+i2+...+im)
# 所以我们需要知道Si = Sk+1 时：1. 下标 i 出现的次数 m 2. 下标 i 之和
# 借助两个哈希表来做到，在遍历下标 k 的同时，一个哈希表统计 Sk 的出现次数，另一个哈希表统计值为 Sk 的下标之和。
from collections import Counter

class Solution3:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        s = [0]
        for val in arr:
            s.append(s[-1] ^ val)

        cnt, total = Counter(), Counter()
        ans = 0
        for k in range(n):
            if s[k + 1] in cnt:
                ans += cnt[s[k + 1]] * k - total[s[k + 1]]
            cnt[s[k]] += 1
            total[s[k]] += k

        return ans

# 在计算异或前缀和的同时计算答案，从而做到仅遍历 arr 一次就计算出答案。
class Solution4:
    def countTriplets(self, arr: List[int]) -> int:
        cnt, total = Counter(), Counter()
        ans = s = 0

        for k, val in enumerate(arr):
            if (t := s ^ val) in cnt:
                ans += cnt[t] * k - total[t]
            cnt[s] += 1
            total[s] += k
            s = t

        return ans

