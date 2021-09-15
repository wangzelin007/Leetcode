# 524. Given a string s and a string array dictionary, return the longest string in the dictionary that can be formed by deleting some of the given string characters.
# If there is more than one possible result, return the longest word with the smallest lexicographical order.
# If there is no possible result, return the empty string.
#
# Example 1:
# Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
# Output: "apple"
# Example 2:
# Input: s = "abpcplea", dictionary = ["a","b","c"]
# Output: "a"
#
# Constraints:
# 1 <= s.length <= 1000
# 1 <= dictionary.length <= 1000
# 1 <= dictionary[i].length <= 1000
# s and dictionary[i] consist of lowercase English letters.
from typing import List
from functools import cmp_to_key


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def mycmp(x, y):
            if len(x) - len(y) > 0:
                return -1
            elif len(x) == len(y) and x < y:
                return -1
            else:
                return 1
        dictionary.sort(key=cmp_to_key(mycmp))
        n = len(s)
        for d in dictionary:
            k = len(d)
            if n < k:
                continue
            i, j = 0, 0
            while i < n and j < k:
                if s[i] == d[j]:
                    j += 1
                i += 1
            if j == k:
                return d
        return ""

    def findLongestWord2(self, s: str, dictionary: List[str]) -> str:
        res = ""
        for d in dictionary:
            i = j = 0
            while i < len(s) and j < len(d):
                if s[i] == d[j]:
                    j += 1
                i += 1
                if j == len(d):
                    if j > len(res) or (j == len(res) and d < res):
                        res = d
        return res

    def findLongestWord3(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))
        for d in dictionary:
            i = j = 0
            while i < len(s) and j < len(d):
                if s[i] == d[j]:
                    j += 1
                i += 1
            if j == len(d):
                return d
        return ""

    def findLongestWord4(self, s: str, dictionary: List[str]) -> str:
        m = len(s)
        f = [[0] * 26 for _ in range(m)]
        f.append([m] * 26)
        # 通过预处理，得到：对于 s 的每一个位置，从该位置开始往后每一个字符第一次出现的位置。
        # [[0, 1, 3, 8, 6, 8, 8, 8, 8, 8, 8, 5, 8, 8, 8, 2, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
        #  [7, 1, 3, 8, 6, 8, 8, 8, 8, 8, 8, 5, 8, 8, 8, 2, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
        #  [7, 8, 3, 8, 6, 8, 8, 8, 8, 8, 8, 5, 8, 8, 8, 2, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
        #  [7, 8, 3, 8, 6, 8, 8, 8, 8, 8, 8, 5, 8, 8, 8, 4, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
        #  [7, 8, 8, 8, 6, 8, 8, 8, 8, 8, 8, 5, 8, 8, 8, 4, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
        #  [7, 8, 8, 8, 6, 8, 8, 8, 8, 8, 8, 5, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
        #  [7, 8, 8, 8, 6, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
        #  [7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
        #  [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]]
        for i in range(m - 1, -1, -1):
            for j in range(26):
                if ord(s[i]) == j + 97:
                    f[i][j] = i
                else:
                    f[i][j] = f[i + 1][j]

        res = ""
        for t in dictionary:
            match = True
            j = 0
            for i in range(len(t)):
                if f[j][ord(t[i]) - 97] == m:
                    match = False
                    break
                j = f[j][ord(t[i]) - 97] + 1
            if match:
                if len(t) > len(res) or (len(t) == len(res) and t < res):
                    res = t
        return res

def test():
    s = Solution()
    assert s.findLongestWord("abpcplea", ["ale","apple","monkey","plea"]) == "apple"
    assert s.findLongestWord("abpcplea", ["a","b","c"]) == "a"
    assert s.findLongestWord2("abpcplea", ["ale", "apple", "monkey", "plea"]) == "apple"
    assert s.findLongestWord2("abpcplea", ["a", "b", "c"]) == "a"
    assert s.findLongestWord3("abpcplea", ["ale", "apple", "monkey", "plea"]) == "apple"
    assert s.findLongestWord3("abpcplea", ["a", "b", "c"]) == "a"
    assert s.findLongestWord4("abpcplea", ["ale", "apple", "monkey", "plea"]) == "apple"
    assert s.findLongestWord4("abpcplea", ["a", "b", "c"]) == "a"

if __name__ == '__main__':
    test()