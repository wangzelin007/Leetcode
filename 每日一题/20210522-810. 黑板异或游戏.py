# 黑板上写着一个非负整数数组 nums[i] 。
# Alice 和 Bob 轮流从黑板上擦掉一个数字，Alice 先手。
# 如果擦除一个数字后，剩余的所有数字按位异或运算得出的结果等于 0 的话，当前玩家游戏失败。
# (另外，如果只剩一个数字，按位异或运算得到它本身；如果无数字剩余，按位异或运算结果为0。）
# 换种说法就是，轮到某个玩家时，如果当前黑板上所有数字按位异或运算结果等于 0，这个玩家获胜。
# 假设两个玩家每步都使用最优解，当且仅当 Alice 获胜时返回 true。
# 示例：
# 输入: nums = [1, 1, 2]
# 输出: false
# 解释:
# Alice 有两个选择: 擦掉数字 1 或 2。
# 如果擦掉 1, 数组变成 [1, 2]。剩余数字按位异或得到 1 XOR 2 = 3。那么 Bob 可以擦掉任意数字，因为 Alice 会成为擦掉最后一个数字的人，她总是会输。
# 如果 Alice 擦掉 2，那么数组变成[1, 1]。剩余数字按位异或得到 1 XOR 1 = 0。Alice 仍然会输掉游戏。
# 提示：
# 1 <= N <= 1000
# 0 <= nums[i] <= 2^16
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/chalkboard-xor-game
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 要么 A 从偶数开始，要么 A 从基数开始(即B 从偶数开始)
# 使用 S 表示原数组 nums 的异或结果
# S = nums[0]⊕nums[1]⊕...⊕nums[n-1] != 0
# 使用Si 表示踢出 i 元素后的异或结果
# Si⊕nums[i] = S -> Si = S⊕nums[i]
# 下面来论证 A 输的可能性，即无论 A 擦掉哪一个数字都会输，即异或结果均为0
# S0⊕S1⊕...⊕Sn-1=0
# 0 = (S⊕nums[0])(S⊕nums[1])⊕...⊕(S⊕nums[n-1])
# 0 = (S⊕S⊕...⊕S)(nums[0]⊕nums[1]⊕...⊕nums[n-1])
# 0 = 0⊕S
# S = 0 与初始假设 S != 0 矛盾，所以偶数时 A 必胜

from typing import List
from operator import xor

class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0: return True
        xorSum = reduce(xor, nums)
        return xorSum == 0
