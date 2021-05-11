# 给你一个整数数组perm，它是前n个正整数的排列，且n是个 奇数。
# 它被加密成另一个长度为 n - 1的整数数组encoded，满足encoded[i] = perm[i] XOR perm[i + 1]。
# 比方说，如果perm = [1,3,2]，那么encoded = [2,1]。
# 给你encoded数组，请你返回原始数组perm。题目保证答案存在且唯一。
# 示例 1：
# 输入：encoded = [3,1]
# 输出：[1,2,3]
# 解释：如果 perm = [1,2,3] ，那么 encoded = [1 XOR 2,2 XOR 3] = [3,1]
# 示例 2：
# 输入：encoded = [6,5,4,6]
# 输出：[2,4,1,5,3]
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/decode-xored-permutation
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

# perm = [A, B, C, D, E]，那么encoded = [AB, BC, CD, DE]；
# ABCDE ^ BCDE = A
# B = A ^ AB
# C = B ^ BC
# ...
class Solution1:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded)
        res = []

        ABCDE = 0
        for i in range(1, n+2):
            ABCDE ^= i
        BCDE = 0
        for i in range(1, n, 2):
            BCDE ^= encoded[i]
        A = ABCDE ^ BCDE
        res.append(A)

        for i in range(n):
            res.append(res[-1]^encoded[i])
        return res

# 思路一样
# 使用了reduce
from functools import reduce
from operator import xor
class Solution2:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        total = reduce(xor, range(1, n + 1))
        odd = 0
        for i in range(1, n - 1, 2):
            odd ^= encoded[i]

        perm = [total ^ odd]
        for i in range(n - 1):
            perm.append(perm[-1] ^ encoded[i])
        print(perm)
        return perm

if __name__ == '__main__':
    s = Solution2()
    encode = [6,5,4,6]
    s.decode(encode)