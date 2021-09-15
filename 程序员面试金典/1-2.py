# Given two strings,write a method to decide if one is a permutation of the other.
#
# Example 1:
# Input: s1 = "abc", s2 = "bca"
# Output: true
# Example 2:
# Input: s1 = "abc", s2 = "bad"
# Output: false
# Note:
# 0 <= len(s1) <= 100
# 0 <= len(s2) <= 100
from collections import Counter


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return sorted(s1) == sorted(s2)

    def CheckPermutation2(self, s1: str, s2: str) -> bool:
        dic1 = {}
        dic2 = {}
        # alphabet = collections.defaultdict(int)
        for i in range(len(s1)):
            dic1[s1[i]] = dic1.get(s1[i], 0) + 1
            dic2[s2[i]] = dic2.get(s2[i], 0) + 1
        return dic1 == dic2

    def CheckPermutation3(self, s1: str, s2: str) -> bool:
        return Counter(s1) == Counter(s2)

    # "singletons" 171723556210517324103152396419465216
    # "concluding" 171723556210517324103152396419465216
    # 此方法不通！，可以构造出和一样的字符串
    def CheckPermutation4(self, s1: str, s2: str) -> bool:
        result = 0
        if len(s1) != len(s2):
            return False
        for i in range(len(s1)):
            result += 1 << ord(s1[i])
            result -= 1 << ord(s2[i])
        return result == 0

def test():
    s = Solution()
    s1 = 'abc'
    s2 = 'cab'
    assert s.CheckPermutation(s1, s2) == s.CheckPermutation2(s1, s2) == s.CheckPermutation3(s1, s2) == True
    s3 = 'abc'
    s4 = 'bcd'
    assert s.CheckPermutation(s3, s4) == s.CheckPermutation2(s3, s4) == s.CheckPermutation3(s3, s4) == False

if __name__ == '__main__':
    test()