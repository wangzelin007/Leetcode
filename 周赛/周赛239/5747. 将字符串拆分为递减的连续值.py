
class Solution:
    def dfs(self, s: str, start: int, last: int):
        if self.ans:
            return

        n = len(s)
        if start == n:
            self.ans = True
            return

        now = 0
        hi = n if start != 0 else n - 1
        for i in range(start, hi):
            now = now * 10 + ord(s[i]) - ord('0')
            if start == 0 or now == last - 1:
                self.dfs(s, i + 1, now)
            if start != 0 and now >= last:
                return

    def splitString(self, s: str) -> bool:
        if len(s) == 1:
            return False

        self.ans = False
        self.dfs(s, 0, 0)
        return self.ans