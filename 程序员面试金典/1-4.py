# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters.
# The palindrome does not need to be limited to just dictionary words.
#
# Example1:
# Input: "tactcoa"
# Output: true（permutations: "tacocat"、"atcocta", etc.）

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        result = 0
        for c in s:
            result ^= 1 << ord(c)
        return result & (result - 1) == 0

def test():
    s = Solution()
    assert s.canPermutePalindrome('tactcoa') == True

if __name__ == '__main__':
    test()