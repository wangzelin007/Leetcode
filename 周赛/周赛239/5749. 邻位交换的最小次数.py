class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        l = list(num)
        o = list(num)
        n = len(l)
        for _ in range(k):
            for i in range(n - 2, -1, -1):
                if l[i] < l[i + 1]:
                    break
            for j in range(n - 1, -1, -1):
                if l[j] > l[i]:
                    break
            l[i], l[j] = l[j], l[i]
            l[i + 1:] = l[i + 1:][::-1]

        ans = 0
        for _ in range(n):
            if l[0] == o[0]:
                l.pop(0)
                o.pop(0)
            else:
                p = o.index(l[0])
                l.pop(0)
                o.pop(p)
                ans += p
        return ans