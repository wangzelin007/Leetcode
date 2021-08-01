# Given n pairs of parentheses,
# write a function to generate all combinations of well-formed parentheses.
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Input: n = 1
# Output: ["()"]
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.n = n
        self._dfs(0, 0, "")
        return self.res

    def _dfs(self, left, right, tmp):
        if left == right == self.n:
            self.res.append(tmp)
            return
        if left < self.n:
            self._dfs(left + 1 , right, tmp + "(")
        if right < self.n and right < left:
            self._dfs(left, right + 1, tmp + ")")

def test():
    n = 3
    s = Solution()
    print(s.generateParenthesis(3))

if __name__ == '__main__':
    test()