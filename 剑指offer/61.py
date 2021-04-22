# 从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
# 2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。
# A 不能视为 14。
# 示例1:
# 输入: [1,2,3,4,5]
# 输出: True
# 示例2:
# 输入: [0,0,1,2,5]
# 输出: True
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution1:
    def isStraight(self, nums: List[int]) -> bool:
        dic = set()
        ma, mi = 0, 14
        for num in nums:
            if num == 0: continue
            if num in dic: return False
            dic.add(num)
            ma = max(ma, num)
            mi = min(mi, num)
        return ma-mi < 5

class Solution2:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        jump = 0
        for index, num in enumerate(nums):
            if num == 0: jump += 1
            elif num == nums[index-1]: return False
        return nums[-1] - nums[jump] < 5

if __name__ == '__main__':
    s1 = Solution1()
    s2 = Solution2()
    nums = [1,2,3,4,5]
    assert s1.isStraight(nums) == s2.isStraight(nums) == True
    nums = [0,0,1,2,5]
    assert s1.isStraight(nums) == s2.isStraight(nums) == True
    nums = [0,1,2,5,6]
    assert s1.isStraight(nums) == s2.isStraight(nums) == False