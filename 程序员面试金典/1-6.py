# Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2blc5a3.
# If the "compressed" string would not become smaller than the original string, your method should return the original string.
# You can assume the string has only uppercase and lowercase letters (a - z).
#
# Example 1:
# Input: "aabcccccaaa"
# Output: "a2b1c5a3"
# Example 2:
# Input: "abbccd"
# Output: "abbccd"
# Explanation:
# The compressed string is "a1b2c2d1", which is longer than the original string.
#
# Note:
# 0 <= S.length <= 50000


class Solution:
    def compressString(self, S: str) -> str:
        res = ''
        pre = ''
        cnt = 1
        for c in S:
            if c == pre:
                cnt += 1
            else:
                if pre != '':
                    res += pre + str(cnt)
                cnt = 1
                pre = c
        res += pre + str(cnt)
        return res if len(res) < len(S) else S

    def compressString2(self, S: str) -> str:
        N = len(S)
        res = ''
        i = 0
        while i < N:
            j = i
            while j < N and S[j] == S[i]:
                j += 1
            res += S[i] + str(j - i)
            i = j
        return res if len(res) < len(S) else S

def test():
    s = Solution()
    assert s.compressString("aabcccccaaa") == "a2b1c5a3"
    assert s.compressString("abbccd") == "abbccd"
    assert s.compressString2("aabcccccaaa") == "a2b1c5a3"
    assert s.compressString2("abbccd") == "abbccd"
    assert s.compressString2("") == ""

if __name__ == '__main__':
    test()