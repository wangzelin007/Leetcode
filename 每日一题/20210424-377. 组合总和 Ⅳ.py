# 给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。
# 请你从 nums 中找出并返回总和为 target 的元素组合的个数。
# 题目数据保证答案符合 32 位整数范围。
# 示例 1：
# 输入：nums = [1,2,3], target = 4
# 输出：7
# 解释：
# 所有可能的组合为：
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# 请注意，顺序不同的序列被视作不同的组合。
# 示例 2：
# 输入：nums = [9], target = 3
# 输出：0
# 提示：
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 1000
# nums 中的所有元素 互不相同
# 1 <= target <= 1000
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/combination-sum-iv
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
# 递归是自顶向下的计算方式（大问题->小问题），而动态规划是自底向上的计算方式（小问题->大问题）。
# 递归
class Solution1:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if target < 0: return 0
        if target == 0: return 1
        res = 0
        for num in nums:
            res += self.combinationSum4(nums, target-num)
        return res

# 记忆化递归
# 关键思路在于避免重复计算，所以初始化时，dp=[-1] * (target+1)
# 如果该位置值不是-1，说明已经计算过直接拿过来使用。
class Solution2:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.dp = [-1] * (target + 1)
        self.dp[0] = 1
        return self.dfs(nums, target)

    def dfs(self, nums, target):
        if target < 0: return 0
        # if target == 0: return 1 # 这句话多了，笔记dp[0] = 1 已经初始化了呀
        if self.dp[target] != -1: return self.dp[target]
        res = 0
        for num in nums:
            res += self.dfs(nums, target-num)
        self.dp[target] = res # 忘记更新dp了，小老弟。
        return res

# 动态规划
# for num in nums:
#     dp[i] += dp[i-num]
class Solution3:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]
        return dp[target]

if __name__ == '__main__':
    s = Solution2()
    nums = [1,2,3]; target = 4
    print(s.combinationSum4(nums, target))
