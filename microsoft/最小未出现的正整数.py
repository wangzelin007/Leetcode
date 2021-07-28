class Solution:

    def firstMissPositive(self, nums: list) -> int:
        if not nums:
            return 1
        for idx, num in enumerate(nums):
            while nums[idx] != idx + 1 and 0 < nums[idx] <= len(nums):
                value = nums[idx]
                if nums[idx] == nums[value-1]:
                    break
                nums[value-1], nums[idx] = nums[idx], nums[value-1]
        for idx, num in enumerate(nums):
            if idx + 1 != num:
                return idx + 1
        return len(nums) + 1

def test():
    s = Solution()
    nums = [-1,1,5,3,4,7,8]
    assert s.firstMissPositive(nums) == 2
    nums = [1, 3, 6, 4, 1, 2]
    assert s.firstMissPositive(nums) == 5
    nums = [1, 2, 3]
    assert s.firstMissPositive(nums) == 4
    nums = [-1, -3]
    assert s.firstMissPositive(nums) == 1

if __name__ == '__main__':
    test()