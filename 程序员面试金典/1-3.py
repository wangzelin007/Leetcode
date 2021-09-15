# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the additional characters,
# and that you are given the "true" length of the string.
# (Note: If implementing in Java,please use a character array so that you can perform this operation in place.)
#
# Example 1:
# Input: "Mr John Smith ", 13
# Output: "Mr%20John%20Smith"
# Example 2:
# Input: "              ", 5
# Output: "%20%20%20%20%20"
#
# Note:
# 0 <= S.length <= 500000

class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        return S[:length].replace(' ', '%20')

    def replaceSpaces2(self, S: str, length: int) -> str:
        res = []
        for c in S[:length]:
            if c == ' ':
                c = '%20'
            res.append(c)
        return ''.join(res)

def test():
    sol = Solution()
    S1 = "Mr John Smith "
    S2 = "              "
    assert sol.replaceSpaces(S1, 13) == "Mr%20John%20Smith" == sol.replaceSpaces2(S1, 13)
    assert sol.replaceSpaces(S2, 5) == "%20%20%20%20%20" == sol.replaceSpaces2(S2, 5)

if __name__ == '__main__':
    test()

