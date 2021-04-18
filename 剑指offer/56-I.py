# 一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。
# 请写程序找出这两个只出现一次的数字。
# 要求时间复杂度是O(n)，空间复杂度是O(1)。
# 示例 1：
# 输入：nums = [4,1,4,6]
# 输出：[1,6] 或 [6,1]
# 示例 2：
# 输入：nums = [1,2,10,4,1,4,3,3]
# 输出：[2,10] 或 [10,2]
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 算法流程：
# 1. 遍历 nums 执行异或
# 2. 循环左移计算 h
# 3. 通过 h 拆分 nums 为两个子数组：
# 4. 分别遍历两个子数组执行异或

from typing import List

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        a, b, x = 0, 0, 0
        h = 1
        for num in nums:
            x ^= num
        while (x & h == 0):
            h <<= 1
        for num in nums:
            if num & h == 0: a ^= num
            else: b ^= num
        return [a, b]

if __name__ == '__main__':
    s = Solution()
    nums = [4,1,4,6]
    assert s.singleNumbers(nums) in [[1,6], [6,1]]
    nums = [1,2,10,4,1,4,3,3]
    assert s.singleNumbers(nums) in [[2,10], [10,2]]