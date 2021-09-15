# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
#
# Example 1:
#
# Input: s = "leetcode"
# Output: false
# Example 2:
#
# Input: s = "abc"
# Output: true


class Solution:
    def isUnique(self, astr: str) -> bool:
        return len(astr) == len(set(list(astr)))

    def isUnique2(self, astr: str) -> bool:
        mark = 0
        for s in astr:
            move_bit = ord(s) - ord('a')
            if mark & 1 << move_bit != 0:
                return False
            else:
                mark |= 1 << move_bit
        return True

if __name__ == '__main__':
    s = Solution()
    assert s.isUnique(astr='leetcode') == False == s.isUnique2(astr='leetcode')
    assert s.isUnique(astr='abc') == True == s.isUnique2(astr='abc')