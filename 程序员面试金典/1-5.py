# There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.
# Example1:
# Input:
# first = "pale"
# second = "ple"
# Output: True
# Example2:
# Input:
# first = "pales"
# second = "pal"
# Output: False

# dp
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        # insert delete replace same
        # dp[i][j]
        # i 代表 first j 代表 second dp[i][j] 代表需要的操作次数
        m = len(first)
        n = len(second)
        first = " " + first
        second = " " + second
        if abs(m - n) > 1:
            return False
        dp = [[float("inf")] * (n + 1) for i in range(m + 1)]
        for i in range(m):
            dp[i][0] = i
        for j in range(n):
            dp[0][j] = j
        dp[0][0] = 0
        if m >= 1:
            dp[1][0] = 1
        if n >= 1:
            dp[0][1] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i][j - 1] + 1, dp[i - 1][j] + 1)
                if first[i] == second[j]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
                else:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)
        return dp[m][n] <= 1

    def oneEditAway2(self, first: str, second: str) -> bool:
        m = len(first)
        n = len(second)
        if abs(m-n) > 1:
            return False
        if m < n:
            return self.oneEditAway2(second, first)
        for i in range(n):
            if first[i] != second[i]:
                if m == n:
                    return first[i + 1:] == second[i + 1:] if i != n-1 else True
                else:
                    return first[i+1:] == second[i:] if i != n-1 else False
        return True

def test():
    s = Solution()
    assert s.oneEditAway('a', '') == True == s.oneEditAway2('a', '')
    assert s.oneEditAway('abcde', 'abde') == True == s.oneEditAway2('abcde', 'abde')
    assert s.oneEditAway('', 'a') == True == s.oneEditAway2('', 'a')
    assert s.oneEditAway('b', 'a') == True == s.oneEditAway2('b', 'a')
    assert s.oneEditAway('teacher', 'beacher') == True == s.oneEditAway2('teacher', 'beacher')
    assert s.oneEditAway('teacher', 'teachy') == False == s.oneEditAway2('teacher', 'teachy')

if __name__ == '__main__':
    test()