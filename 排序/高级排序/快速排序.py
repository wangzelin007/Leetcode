# 快速排序原理：
# 快速排序算法有两个核心点，分别为 “哨兵划分” 和 “递归” 。
# 哨兵划分操作： 以数组某个元素（一般选取首元素）为 基准数 ，将所有小于基准数的元素移动至其左边，大于基准数的元素移动至其右边。
# 递归： 对 左子数组 和 右子数组 递归执行 哨兵划分，直至子数组长度为 1 时终止递归，即可完成对整个数组的排序。
# 快速排序和 二分法 的原理类似，都是以 log 时间复杂度实现搜索区间缩小。
# 时间复杂度 O(NlogN) ： 库函数、快排等排序算法的平均时间复杂度为 O(NlogN) 。
# 空间复杂度 O(N) ： 快速排序的递归深度最好（平均）为 O(logN) ，最差情况（即输入数组完全倒序）为 O(N)。
class Solution:
    def getLeastNumbers(self, arr: list[int], k: int) -> list[int]:
        def quick_sort(arr, l, r):
            # 子数组长度为 1 时终止递归
            if l >= r: return
            # 哨兵划分操作（以 arr[l] 作为基准数）
            i, j = l, r
            while i < j:
                while i < j and arr[j] >= arr[l]: j -= 1
                while i < j and arr[i] <= arr[l]: i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[l], arr[i] = arr[i], arr[l]
            # 递归左（右）子数组执行哨兵划分
            quick_sort(arr, l, i - 1)
            quick_sort(arr, i + 1, r)

        quick_sort(arr, 0, len(arr) - 1)
        return arr[:k]

# 作者：jyd
# 链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/solution/jian-zhi-offer-40-zui-xiao-de-k-ge-shu-j-9yze/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
