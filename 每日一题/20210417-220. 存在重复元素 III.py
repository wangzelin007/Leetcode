# 给你一个整数数组 nums 和两个整数k 和 t 。
# 请你判断是否存在两个下标 i 和 j，使得abs(nums[i] - nums[j]) <= t ，同时又满足 abs(i - j) <= k 。
# 如果存在则返回 true，不存在返回 false。
# 示例1：
# 输入：nums = [1,2,3,1], k = 3, t = 0
# 输出：true
# 示例 2：
# 输入：nums = [1,0,1,1], k = 1, t = 2
# 输出：true
# 示例 3：
# 输入：nums = [1,5,9,1,5,9], k = 2, t = 3
# 输出：false
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/contains-duplicate-iii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
from sortedcontainers import SortedSet, SortedList
import bisect

class Solution1:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # 可以用set的原因是t>=0,相等时走到了33行
        st = SortedSet()
        left, right = 0, 0
        res = 0
        while right < len(nums):
            if right - left > k:
                st.remove(nums[left])
                left += 1
            index = bisect.bisect_left(st, nums[right] - t)
            # index >= 0 and index < len(st) 代表 nums[right]-t 可以替代原有的一个元素，否则差值肯定大于t
            if st and index >= 0 and index < len(st) and abs(st[index] - nums[right]) <= t:
                return True
            st.add(nums[right])
            right += 1
        return False

# 清晰一些，两边的元素都比较一下。
class Solution2:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # O(N logk)
        window = SortedList()
        for i in range(len(nums)):
            # len(window) == k
            if i > k:
                window.remove(nums[i - 1 - k])
            window.add(nums[i])
            idx = bisect.bisect_left(window, nums[i])
            if idx > 0 and abs(window[idx] - window[idx-1]) <= t:
                return True
            if idx < len(window) - 1 and abs(window[idx+1] - window[idx]) <= t:
                return True
        return False

# todo
# 桶排序，大概思路是构造 0~t t+1~2t+1 2t+2~3t+2 ... 的桶
# 比较相邻两个桶
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        def getIdx(u):
            return (u+1) // size - 1 if u < 0 else u // size

        map = {}
        size = t + 1
        for i,u in enumerate(nums):
            idx = getIdx(u)
            # 目标桶已存在（桶不为空），说明前面已有 [u - t, u + t] 范围的数字
            if idx in map:
                return True
            # 检查相邻的桶
            l, r = idx - 1, idx + 1
            if l in map and abs(u - map[l]) <= t:
                return True
            if r in map and abs(u - map[r]) <= t:
                return True
            # 建立目标桶
            map[idx] = u
            # 维护个数为k
            if i >= k:
                map.pop(getIdx(nums[i-k]))

        return False

if __name__ == '__main__':
    s = Solution()
    nums, k, t = [1,5,10,1], 3, 0
    print(s.containsNearbyAlmostDuplicate(nums, k, t))