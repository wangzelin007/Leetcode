from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = float('inf')
        for index, num in enumerate(nums):
            if num != target: continue
            else:
                res = min(res, abs(index-start))
        return res

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        return min([abs(i - start) for i in range(len(nums)) if nums[i] == target])

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4,5]; target = 5; start = 3
    print(s.getMinDistance(nums, target, start))
    nums = [1]; target = 1; start = 0
    print(s.getMinDistance(nums, target, start))
    nums = [1,1,1,1,1,1,1,1,1,1]; target = 1; start = 0
    print(s.getMinDistance(nums, target, start))