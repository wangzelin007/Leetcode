class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        # 感觉可以使用dp
        # 假设已经找到了 4 16 4
        # 就可以继续找 有没有两个 2
        # 假设nums 中的最大值为 maxn minn

        # 1. 模拟 可能会超时
        # 由最大值开始，诶个找，并记录最大长度

        # 2. 模拟
        # 而且先算出来可能找到的最大长度是多少？
        # 也可以直接估算为 n
        # 如果是16 -> 2 4 16 4 2 -> 5
        # 公式是: 2^4 = 16 -> 1
        #        2^2 = 4  -> 2
        #        2        -> 2
        # 由最小值开始，诶个找，并记录长度

        # 先排序
        # 假设已dp[x] 前 x 的最大长度是 dp[x] 了，且最大值肯定是最后一个值 nums[x - 1]
        # 2 2 4
        # 2 2 4 4 16
        # 如果nums[i] == nums[i - 1] 且 nums[i + 1] = nums[i]^2
        # dp[i + 1] = dp[i - 1] + 2
        # 再使用 j 遍历
        # nums[i + 1] = max(dp[j] + 2) (需要满足nums[j] ~ nums[i + 1] 中存在 num[j] nums[j] ^ 2)
        n = len(nums)
        dp = [1] * n  # 长度为 n, 如果代表取的最后一位的下标呢？, 所以nums中都需要 -1  dp[0] ~ dp[n - 1] -> nums[0] -> nums[n - 1]
        nums.sort()
        # print(nums)
        for i in range(2, n):
            if nums[i] != 1 and i <= n - 2 and nums[i] == nums[i - 1] and nums[i + 1] == nums[i] ** 2:
                dp[i + 1] = dp[i - 1] + 2
                # print(1, dp)
            else:
                for j in range(i):
                    if nums[j] != 1 and nums[j] in nums[j + 1: i + 1] and nums[j] ** 2 in nums[j + 1: i + 1]:
                        dp[i] = max(dp[i], dp[j] + 2)
                    elif nums[j] == 1 and nums[j + 1: i + 1].count(1) > 1:
                        dp[i] = max(dp[i], dp[j] + 2)
                        print('ha', 'i=', i, nums[j], nums[j + 1: i + 1])
                        # print(2, dp)
        print(dp)
        return max(dp)

nums = [4,36,9,16,1,1,4,121,64,4]
nums = [1,1,1,1,1,1,1,1,1,1]
s = Solution()
s.maximumLength(nums)