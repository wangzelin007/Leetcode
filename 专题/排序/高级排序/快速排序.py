# 快速排序原理：
# 快速排序算法有两个核心点，分别为 “哨兵划分” 和 “递归” 。
# 哨兵划分操作： 以数组某个元素（一般选取首元素）为 基准数 ，将所有小于基准数的元素移动至其左边，大于基准数的元素移动至其右边。
# 递归： 对 左子数组 和 右子数组 递归执行 哨兵划分，直至子数组长度为 1 时终止递归，即可完成对整个数组的排序。
# 快速排序和 二分法 的原理类似，都是以 log 时间复杂度实现搜索区间缩小。
# 时间复杂度 O(NlogN) ： 库函数、快排等排序算法的平均时间复杂度为 O(NlogN) 。
# 空间复杂度 O(N) ： 快速排序的递归深度最好（平均）为 O(logN) ，最差情况（即输入数组完全倒序）为 O(N)。
from typing import List
import random
from copy import deepcopy

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        self.quick_sort(arr, 0, len(arr) - 1)
        return arr[:k]

    def quick_sort(self, arr, l, r):
        # 子数组长度为 1 时终止递归
        if l >= r: return
        # m = self.partition1(arr, l, r)
        m = self.partition2(arr, l, r)
        # 递归左（右）子数组执行哨兵划分
        self.quick_sort(arr, l, m - 1)
        self.quick_sort(arr, m + 1, r)

    def quick_sort2(self, arr, l, r):
        if l >= r: return
        equalArea = self.netherlandsFlags(arr,l, r)
        self.quick_sort2(arr, l, equalArea[0] - 1)
        self.quick_sort2(arr, equalArea[1] + 1, r)

    def quick_sort3(self, arr, l, r):
        if l >= r: return
        rand = l + int(random.uniform(0, 1) * (r - l + 1))
        arr[rand], arr[r] = arr[r], arr[rand]
        equalArea = self.netherlandsFlags(arr,l, r)
        self.quick_sort2(arr, l, equalArea[0] - 1)
        self.quick_sort2(arr, equalArea[1] + 1, r)

    def partition1(self, arr, l, r):
        # 以arr[r] 作为基准数
        i = l
        less, more = l - 1, r
        while i < more:
            if arr[i] == arr[r]: i += 1
            elif arr[i] < arr[r]:
                arr[less+1], arr[i] = arr[i], arr[less+1]
                less += 1
                i += 1
            else:
                arr[more-1], arr[i] = arr[i], arr[more-1]
                more -= 1
        arr[r], arr[i] = arr[i], arr[r]
        return i

    def partition2(self, arr, l, r):
        # 哨兵划分操作（以 arr[l] 作为基准数）
        i, j = l, r
        while i < j:
            while i < j and arr[j] >= arr[l]: j -= 1
            while i < j and arr[i] <= arr[l]: i += 1
            arr[i], arr[j] = arr[j], arr[i]
        arr[l], arr[i] = arr[i], arr[l]
        return i

    def netherlandsFlags(self, li, L, R):
        # 荷兰国旗版本，可以去掉重复的若干数
        if L > R: return [-1, -1]
        if L == R: return [L, R]
        less = L - 1
        more = R
        index = L
        while index < more:
            if li[index] == li[R]:
                index += 1
            elif li[index] < li[R]:
                li[index], li[less+1] = li[less+1], li[index]
                less += 1
                index += 1
            else:
                li[index], li[more-1] = li[more-1], li[index]
                more -= 1
        li[more], li[R] = li[R], li[more]
        # print(li)
        return [less+1, more]

def test():
    arr = [random.randint(0,100) for _ in range(100)]
    arr1 = deepcopy(arr)
    arr2 = deepcopy(arr)
    arr3 = deepcopy(arr)
    s = Solution()
    # print(s.getLeastNumbers(arr, 99))
    s.quick_sort(arr1, 0, 99)
    s.quick_sort2(arr2, 0, 99)
    s.quick_sort3(arr3, 0, 99)
    assert arr1 == arr2 == arr3

if __name__ == '__main__':
    test()

# 快排改进 todo
# 随机选取哨兵，然后与 l 交换
# https://zhuanlan.zhihu.com/p/142391758

# 作者：jyd
# 链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/solution/jian-zhi-offer-40-zui-xiao-de-k-ge-shu-j-9yze/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
