# Design an algorithm to find the smallest K numbers in an array.
# Example:
# Input:  arr = [1,3,5,7,2,4,6,8], k = 4
# Output:  [1,2,3,4]
# Note:
# 0 <= len(arr) <= 100000
# 0 <= k <= min(100000, len(arr))
import heapq
from typing import List


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        if len(arr) <= k:
            return sorted(arr)
        heap = [-arr[i] for i in range(k)]
        heapq.heapify(heap)
        for i in range(k, len(arr)):
            heapq.heappush(heap, -arr[i])
            heapq.heappop(heap)
        ref = [-i for i in heap]
        return sorted(ref)

def test():
    arr = [1,3,5,7,2,4,6,8]
    k = 4
    s = Solution()
    ref = s.smallestK(arr, k)
    print(ref)

if __name__ == '__main__':
    test()