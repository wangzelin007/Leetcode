# 给你一个整数数组 nums ，返回 nums[i] XOR nums[j] 的最大运算结果，其中 0 ≤ i ≤ j < n 。
# 进阶：你可以在 O(n) 的时间解决这个问题吗？
# 示例 1：
# 输入：nums = [3,10,5,25,2,8]
# 输出：28
# 解释：最大运算结果是 5 XOR 25 = 28.
# 示例 2：
# 输入：nums = [0]
# 输出：0
# 示例 3：
# 输入：nums = [2,4]
# 输出：6
# 示例 4：
# 输入：nums = [8,10,2]
# 输出：10
# 示例 5：
# 输入：nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# 输出：127
# 提示：
# 1 <= nums.length <= 2 * 104
# 0 <= nums[i] <= 231 - 1
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Trie:
    def __init__(self, val):
        self.val = val
        self.child = {}


class Solution1:
    def findMaximumXOR(self, nums: List[int]) -> int:
        #取得最大的数的二进制长度 - 1
        # 25 2^4+2^3+2^0 = 11001
        # format(25) = 11001 分别右移 4,3,2,1,0
        L = len(format(max(nums), 'b'))-1

        # 构建前缀树
        root = Trie(-1)

        for n in nums:
            curr = root
            for i in range(L, -1, -1):

                # 从高位到低位构建前缀树
                v = (n >> i) & 1
                if v not in curr.child:
                    curr.child[v] = Trie(v)

                curr = curr.child[v]

        res = 0

        #搜索
        for n in nums:
            curr = root
            total = 0
            for i in range(L, -1, -1): # 先看高位
                v = (n >> i) & 1 # 0 or 1
                if 1-v in curr.child: # 找相反的
                    total = total * 2 + 1 # 可以找到相反的，那么取出这一位
                    curr = curr.child[1-v] # 然后沿着这一位继续往下找
                else:
                    total = total * 2 # 不可以找到相反的，取不到这一位
                    curr = curr.child[v] # 然后沿着取不到的情况继续往下找

            #print(n, total)
            res = max(res, total) # 每次找完一个数，都和之前的结果进行比较

        return res

# todo 前缀树
class Trie2:
    def __init__(self):
        # 左子树指向表示 0 的子节点
        self.left = None
        # 右子树指向表示 1 的子节点
        self.right = None

class Solution2:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # 字典树的根节点
        root = Trie2()
        # 最高位的二进制位编号为 30
        HIGH_BIT = 30

        def add(num: int):
            cur = root
            for k in range(HIGH_BIT, -1, -1):
                bit = (num >> k) & 1
                if bit == 0:
                    if not cur.left:
                        cur.left = Trie2()
                    cur = cur.left
                else:
                    if not cur.right:
                        cur.right = Trie2()
                    cur = cur.right

        def check(num: int) -> int:
            cur = root
            x = 0
            for k in range(HIGH_BIT, -1, -1):
                bit = (num >> k) & 1
                if bit == 0:
                    # a_i 的第 k 个二进制位为 0，应当往表示 1 的子节点 right 走
                    if cur.right:
                        cur = cur.right
                        x = x * 2 + 1
                    else:
                        cur = cur.left
                        x = x * 2
                else:
                    # a_i 的第 k 个二进制位为 1，应当往表示 0 的子节点 left 走
                    if cur.left:
                        cur = cur.left
                        x = x * 2 + 1
                    else:
                        cur = cur.right
                        x = x * 2
            return x

        n = len(nums)
        x = 0
        for i in range(1, n):
            # 将 nums[i-1] 放入字典树，此时 nums[0 .. i-1] 都在字典树中
            add(nums[i - 1])
            # 将 nums[i] 看作 ai，找出最大的 x 更新答案
            x = max(x, check(nums[i]))

        return x

# todo 哈希表
class Solution3:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # 最高位的二进制位编号为 30
        HIGH_BIT = 30

        x = 0
        for k in range(HIGH_BIT, -1, -1):
            seen = set()
            # 将所有的 pre^k(a_j) 放入哈希表中
            for num in nums:
                # 如果只想保留从最高位开始到第 k 个二进制位为止的部分
                # 只需将其右移 k 位
                seen.add(num >> k)

            # 目前 x 包含从最高位开始到第 k+1 个二进制位为止的部分
            # 我们将 x 的第 k 个二进制位置为 1，即为 x = x*2+1
            x_next = x * 2 + 1
            found = False

            # 枚举 i
            for num in nums:
                if x_next ^ (num >> k) in seen:
                    found = True
                    break

            if found:
                x = x_next
            else:
                # 如果没有找到满足等式的 a_i 和 a_j，那么 x 的第 k 个二进制位只能为 0
                # 即为 x = x*2
                x = x_next - 1

        return x

if __name__ == '__main__':
    s = Solution1()
    s.findMaximumXOR(nums = [3,10,5,25,2,8])