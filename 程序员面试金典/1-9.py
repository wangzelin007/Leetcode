# Given two strings, s1 and s2, write code to check if s2 is a rotation of s1
# (e.g.,"waterbottle" is a rotation of"erbottlewat").
# Can you use only one call to the method that checks if one word is a substring of another?
#
# Example 1:
# Input: s1 = "waterbottle", s2 = "erbottlewat"
# Output: True
# Example 2:
# Input: s1 = "aa", s2 = "aba"
# Output: False
#
# Note:
# 0 <= s1.length, s2.length <= 100000


class Solution:
    # 拼接
    def isFlipedString(self, s1: str, s2: str) -> bool:
        return (len(s1) == len(s2)) and (s1 in s2 + s2)

    def isFlipedString2(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2): return False
        if len(s1) == 0: return True
        for i in range(len(s1)):
            if s1[i] == s2[0]:
                if s1[i:] == s2[0:len(s1) - i] and s1[:i] == s2[len(s1) - i:]:
                    return True
        return False

def test():
    s = Solution()
    s1 = "waterbottle"; s2 = "erbottlewat"
    assert s.isFlipedString(s1, s2) == True
    assert s.isFlipedString2(s1, s2) == True
    s1 = "aa"; s2 = "aba"
    assert s.isFlipedString(s1, s2) == False
    assert s.isFlipedString2(s1, s2) == False

if __name__ == '__main__':
    test()




