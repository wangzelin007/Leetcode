from typing import List

class Solution1:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        if n < 1: return n
        i, j = 0, n
        while i < j:
            if nums[i] == val:
                nums[i] == nums[j-1]
                j -= 1
            else:
                i += 1
        return i

class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        if n < 1: return n
        i, j = 0, n - 1
        while i <= j:
            while i <= j and nums[i] != val:
                i += 1
            while i <= j and nums[j] == val:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
        return i


if __name__ == '__main__':
    s = Solution2()
    assert s.removeElement([3,2,2,3], 3) == 2
    assert s.removeElement([2,2,2,3], 3) == 3
    assert s.removeElement([2], 1) == 1
    assert s.removeElement([2], 2) == 0
    assert s.removeElement([2,2,2,2], 2) == 0