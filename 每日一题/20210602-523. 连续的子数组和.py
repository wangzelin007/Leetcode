# 给你一个整数数组 nums 和一个整数k ，编写一个函数来判断该数组是否含有同时满足下述条件的连续子数组：
# 子数组大小 至少为 2 ，且
# 子数组元素总和为 k 的倍数。
# 如果存在，返回 true ；否则，返回 false 。
# 如果存在一个整数 n ，令整数 x 符合 x = n * k ，则称 x 是 k 的一个倍数。
# 示例 1：
# 输入：nums = [23,2,4,6,7], k = 6
# 输出：true
# 解释：[2,4] 是一个大小为 2 的子数组，并且和为 6 。
# 示例 2：
# 输入：nums = [23,2,6,4,7], k = 6
# 输出：true
# 解释：[23, 2, 6, 4, 7] 是大小为 5 的子数组，并且和为 42 。
# 42 是 6 的倍数，因为 42 = 7 * 6 且 7 是一个整数。
# 示例 3：
# 输入：nums = [23,2,6,4,7], k = 13
# 输出：false
# 提示：
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109
# 0 <= sum(nums[i]) <= 231 - 1
# 1 <= k <= 231 - 1
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/continuous-subarray-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

# 同余定理
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        modes = set()
        presum = 0
        for num in nums:
            last = presum
            presum += num
            presum %= k
            print(presum,modes)
            if presum in modes:
                return True
            modes.add(last)
        return False

from collections import defaultdict

# 如何计算次数
class Solution1:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        modes = {}
        presum = 0
        ans = 0
        for num in nums:
            last = presum
            presum += num
            presum %= k
            if presum in modes:
                ans += modes[presum]
            modes[last] = modes.get(last, 0) + 1
        print(ans)
        return ans

if __name__ == '__main__':
    s = Solution()
    s.checkSubarraySum([23,2,6,4,7], 6)
    # [23,25,31,35,42]
    # 5, 1, 1, 5, 0
    s1 = Solution1()
    s1.checkSubarraySum([24,2,6,4,6,6,6,6], 6)
    # 24 2 6 4
    # 2 6 4
    # +2 +3 +4 +5
    s1 = Solution1()
    s1.checkSubarraySum([1,2,3,4,5], 2)