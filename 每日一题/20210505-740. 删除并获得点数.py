# 给你一个整数数组nums，你可以对它进行一些操作。
# 每次操作中，选择任意一个nums[i]，删除它并获得nums[i]的点数。
# 之后，你必须删除每个等于nums[i] - 1或nums[i] + 1的元素。
# 开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。
# 示例 1：
# 输入：nums = [3,4,2]
# 输出：6
# 解释：
# 删除 4 获得 4 个点数，因此 3 也被删除。
# 之后，删除 2 获得 2 个点数。总共获得 6 个点数。
# 示例2：
# 输入：nums = [2,2,3,3,3,4]
# 输出：9
# 解释：
# 删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
# 之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
# 总共获得 9 个点数。
# 提示：
# 1 <= nums.length <= 2 * 104
# 1 <= nums[i] <= 104
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/delete-and-earn
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

# dp[i] 代表 选择了元素 i 后，可以获得的点数
# dp[i] = value(i) * count(i)

class Solution1:
    def deleteAndEarn(self, nums: List[int]) -> int:
        maxVal = max(nums)
        total = [0] * (maxVal + 1)
        for val in nums:
            total[val] += val
        print(total)

        def rob(nums: List[int]) -> int:
            size = len(nums)
            first, second = nums[0], max(nums[0], nums[1])
            for i in range(2,size):
                first, second = second, max(first + nums[i], second)
            return second

        return rob(total)

#  若nums 中不存在某个元素 x，则选择任一小于 x 的元素不会影响到大于 x 的元素的选择。
#  因此我们可以将 nums 排序后，将其划分成若干连续子数组，子数组内任意相邻元素之差不超过 1。
#  对每个子数组按照方法一的动态规划过程计算出结果，累加所有结果即为答案。
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        def rob(nums: List[int]) -> int:
            size = len(nums)
            if size == 1:
                return nums[0]

            first, second = nums[0], max(nums[0], nums[1])
            for i in range(2, size):
                first, second = second, max(first + nums[i], second)
            return second

        n = len(nums)
        ans = 0
        nums.sort()
        total = [nums[0]]
        print(total)
        for i in range(1, n):
            val = nums[i]
            if val == nums[i - 1]:
                total[-1] += val
            elif val == nums[i - 1] + 1:
                total.append(val)
            else:
                ans += rob(total)
                total = [val]

        ans += rob(total)
        return ans

if __name__ == '__main__':
    s = Solution()
    nums = [3,4,2]
    print(s.deleteAndEarn(nums))
    nums = [2,2,3,3,3,4,6]
    print(s.deleteAndEarn(nums))