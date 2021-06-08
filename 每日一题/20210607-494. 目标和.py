# 给你一个整数数组 nums 和一个整数 target 。
# 向数组中的每个整数前添加'+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
# 示例 1：
# 输入：nums = [1,1,1,1,1], target = 3
# 输出：5
# 解释：一共有 5 种方法让最终目标和为 3 。
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# 示例 2：
# 输入：nums = [1], target = 1
# 输出：1
# 提示：
# 1 <= nums.length <= 20
# 0 <= nums[i] <= 1000
# 0 <= sum(nums[i]) <= 1000
# -1000 <= target <= 100
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/target-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
from _collections import defaultdict
# 将dp[i][j]定义为从数组nums中前 i 的元素进行加减可以得到 j 的方法数量。
# dp[i][j] = dp[i-1][j-nums[i]] + dp[i-1][j+nums[i]]
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        Sum = sum(nums)
        # 边界
        if target > Sum or target < -Sum: return 0
        # 初始化
        # 使用defaultdict(int)可以偷懒避免越界
        dp = [defaultdict(int) for i in range(len(nums))]
        dp[0][nums[0]] = 1
        dp[0][-nums[0]] += 1 # nums[0]=0时，dp[0][0]=2
        for i in range(1, len(nums)):
            for j in range(-Sum, Sum+1):
                dp[i][j] = dp[i-1][j-nums[i]] + dp[i-1][j+nums[i]]
        print(dp)
        return dp[len(nums)-1][target]

# todo 背包问题
# 装满背包一般解 dp[j] += dp[j - nums[i]];
# 如果绝对值和为sumValue 所有+数和为 所有负数和为 sumValue-x
# x - (sumValue-x) = 2x - sumValue = target
# x = (sumValue + target) / 2
# 转化为：装满容量为 x 的背包，有几种方法。
# 为什么是 0 1 背包，因为每个物品 num 都只能使用 0 or 1 次
# 步骤：
# 确定dp数组以及下标的含义 dp[j] 表示填满容积为 j 背包的方法数。
# 确定递推公式 dp[j] += dp[j - nums[i]] todo 不太理解为什么可以不考虑nums[i]
# dp数组如何初始化 dp[0] = 1，即装满容量为0的背包，有1种方法，就是装0件物品。
# 确定遍历顺序 todo
# 举例推导dp数组 todo dp数组状态变化图没有理解
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sumValue = sum(nums)
        if target > sumValue or (sumValue + target) % 2 == 1: return 0
        bagSize = (sumValue + target) // 2
        dp = [0] * (bagSize + 1)
        dp[0] = 1 # 装满容量为0的背包，有1种方法，就是装0件物品。
        for i in range(len(nums)):
            for j in range(bagSize, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]
        return dp[bagSize]

if __name__ == '__main__':
    s = Solution()
    nums = [1,1,1,1,1]; target = 3
    s.findTargetSumWays(nums, target)

