# 给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
# 示例:
# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
# 解释:
# 滑动窗口的位置                最大值
# ---------------               -----
# [1 3  -1] -3  5  3  6  7       3
# 1 [3  -1  -3] 5  3  6  7       3
# 1  3 [-1  -3  5] 3  6  7       5
# 1  3  -1 [-3  5  3] 6  7       5
# 1  3  -1  -3 [5  3  6] 7       6
# 1  3  -1  -3  5 [3  6  7]      7
# 提示：
# 你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤输入数组的大小。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# 滑动窗口法
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        if k == 0: return []
        for i in range(k):
            while q and nums[i] > q[-1]:
                q.pop()
            q.append(nums[i])
        res = [q[0]]
        for i in range(k,len(nums)):
            if q[0] == nums[i-k]:
                q.popleft()
            while q and nums[i] > q[-1]:
                q.pop()
            q.append(nums[i])
            res.append(q[0])
        return res

    # 1. 每次都需要向window append i
    # 2. 如果长度足够 (i - window[0] >= k)，window 需要 pop 头部失效的数
    # 3. 如果 x > window 最后一个数，需要清空 window
    # 4. 每轮都要追加 res
    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        window, res = [], []
        for i, x in enumerate(nums):
            if i >= k and i - window[0] >= k:
                window.pop(0)
            while window and x >= nums[window[-1]]:
                window.pop()
            window.append(i)
            if i >= k - 1:
                res.append(nums[window[0]])
        return res

def test():
    s = Solution()
    nums = [1,3,-1,-3,5,3,6,7]; k = 3
    # print(s.maxSlidingWindow(nums, k))
    assert s.maxSlidingWindow(nums, k) == [3,3,5,5,6,7]
    assert s.maxSlidingWindow(nums, k) == s.maxSlidingWindow2(nums, k)
    nums = [1,3,1,2,0,5]; k = 3
    assert s.maxSlidingWindow(nums, k) == [3,3,2,5]
    assert s.maxSlidingWindow(nums, k) == s.maxSlidingWindow2(nums, k)

if __name__ == '__main__':
    test()

