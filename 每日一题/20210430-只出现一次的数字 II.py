# 给你一个整数数组nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。
# 请你找出并返回那个只出现了一次的元素。
# 示例 1：
# 输入：nums = [2,2,3,2]
# 输出：3
# 示例 2：
# 输入：nums = [0,1,0,1,0,1,99]
# 输出：99
# 提示：
# 1 <= nums.length <= 3 * 104
# -231 <= nums[i] <= 231 - 1
# nums 中，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/single-number-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

# 剑指offer 56-II
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = [0] * 32
        for num in nums:
            for j in range(32):
                counts[j] += num & 1 # 低位到高位
                num >>= 1
        res, m = 0, 3
        for i in range(32):
            res <<= 1 # 高位到低位
            res |= counts[31 - i] % m
        # return res if res <= 0x7fffffff else ~(res ^ 0xffffffff) # same
        return res if counts[31] % m == 0 else ~(res^0xffffffff)
