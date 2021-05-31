# 给定一个整数数组和一个整数k，你需要找到该数组中和为k的连续的子数组的个数。
# 示例 1 :
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
# 说明 :
# 数组的长度为 [1, 20,000]。
# 数组中元素的范围是 [-1000, 1000] ，且整数k的范围是[-1e7, 1e7]。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/subarray-sum-equals-k
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
from collections import Counter

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = Counter([0])
        count = pre = 0
        for x in nums:
            pre += x
            if pre - k in mp:
                count += mp[pre - k]
            mp[pre] += 1
        print(count)
        return count

if __name__ == '__main__':
    s = Solution()
    s.subarraySum([1,1,1], 2)