class Solution:
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [False] * (n + 1)  # dp[n] 代表长度为n, 从 0 到 n - 1 的字符串是否可以拼接成
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(0, i):
                try:
                    if dp[j] and (s[j:i] in wordDict):
                        dp[i] = True
                        break
                except Exception as e:
                    print(i, j)
                    print(dp)
                    print(dp[j])
                    print(s[j:i])
                    raise e

        return dp[n]

s = "leetcode"
wordDict = ["leet", "code"]
q139 = Solution()
q139.wordBreak(s, wordDict)