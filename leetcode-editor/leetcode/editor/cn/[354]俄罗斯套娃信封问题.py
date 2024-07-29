from bisect import bisect_left


class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        if not envelopes:
            return 0

        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        f = [envelopes[0][1]]
        for i in range(1, n):
            if (num := envelopes[i][1]) > f[-1]:
                f.append(num)
            else:
                index = bisect_left(f, num)
                print(f, num, index)
                f[index] = num
        print(f)
        return len(f)

s = Solution()
envelopes = [[1,4],[1,3],[1,2], [2,4], [2,3], [2,2], [2,1], [3,4], [3,1]]
s.maxEnvelopes(envelopes)