# 给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。
# 示例 1:
# 输入: nums = [0,1]
# 输出: 2
# 说明: [0, 1] 是具有相同数量0和1的最长连续子数组。
# 示例 2:
# 输入: nums = [0,1,0]
# 输出: 2
# 说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。
# 提示：
# 1 <= nums.length <= 105
# nums[i] 不是 0 就是 1
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/contiguous-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

# 前缀和
# 0 减一 1 加一
# 如果 dict 中存在 cur，说明遇到了满足条件的连续子数组。
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {0: -1}
        cur = 0
        ans = 0
        for index, num in enumerate(nums):
            cur += 1 if num else -1
            if cur in dic:
                ans = max(ans, index - dic[cur])
            else:
                dic[cur] = index
        print(ans)
        return ans

if __name__ == '__main__':
    s = Solution()
    s.findMaxLength([0,1,1,0,1,1,1,0,0,1,1,0,1,0,0,1])