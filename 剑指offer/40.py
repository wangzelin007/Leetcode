# _*_ coding: utf-8 _*_
# 输入整数数组 arr ，找出其中最小的 k 个数。
# 例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
#
# 示例 1：
# 输入：arr = [3,2,1], k = 2
# 输出：[1,2] 或者 [2,1]
#
# 示例 2：
# 输入：arr = [0,1,2,1], k = 1
# 输出：[0]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 老铁，面试用了悲剧
class Solution1(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        arr.sort()
        return arr[0:k] if k else []

# 复习快排
# 快速排序原理：
# 快速排序算法有两个核心点，分别为 “哨兵划分” 和 “递归” 。
# 哨兵划分操作： 以数组某个元素（一般选取首元素）为 基准数 ，将所有小于基准数的元素移动至其左边，大于基准数的元素移动至其右边。
# 如下图所示，为哨兵划分操作流程。
# 通过一轮 哨兵划分 ，可将数组排序问题拆分为 两个较短数组的排序问题 （本文称之为左（右）子数组）。
# 递归： 对 左子数组 和 右子数组 递归执行 哨兵划分，直至子数组长度为 1 时终止递归，即可完成对整个数组的排序。
class Solution2(object):
    def getLeastNumbers(self, arr, k):
        def quick_sort(l, r):
            if l >= r: return
            i, j = l, r
            while i < j:
                while i < j and arr[j] >= arr[l]: j -= 1
                while i < j and arr[i] <= arr[l]: i += 1
                # 为什么先j后i?
                # 因为需要ij同时指向小于arr[l]的数，哨兵可以来到正确的位置。
                # 反过来就是ij同时指向大于arr[l]的数，此时需要哨兵为最后一个即r才行。
                # while i < j and arr[j] >= arr[l]: j -= 1 （r为哨兵）
                arr[i], arr[j] = arr[j], arr[i]
            arr[i], arr[l] = arr[l], arr[i]
            quick_sort(l, i-1)
            quick_sort(i+1, r)

        quick_sort(0, len(arr)-1)
        return arr[:k]

# 快排 + 判断
# 据快速排序原理，如果某次哨兵划分后 基准数正好是第 k+1 小的数字 ，那么此时基准数左边的所有数字便是题目所求的 最小的 k 个数 。
# 根据此思路，考虑在每次哨兵划分后，判断基准数在数组中的索引是否等于 k ，若 true 则直接返回此时数组的前 k 个数字即可。
#
# 算法流程：
# getLeastNumbers() 函数：
# 1. 若 k 大于数组长度，则直接返回整个数组；
# 2. 执行并返回 quick_sort() 即可；
# quick_sort() 函数：
# 注意，此时 quick_sort() 的功能不是排序整个数组，而是搜索并返回最小的 k 个数。
# 1. 哨兵划分：
# 划分完毕后，基准数为 arr[i] ，左 / 右子数组区间分别为 [l, i - 1], [i + 1, r] ；
# 2. 递归或返回：
# 若 k < i ，代表第 k + 1 小的数字在 左子数组 中，则递归左子数组；
# 若 k > i ，代表第 k + 1 小的数字在 右子数组 中，则递归右子数组；
# 若 k = i ，代表此时 arr[k] 即为第 k + 1 小的数字，则直接返回数组前 k 个数字即可；
class Solution3(object):
    def getLeastNumbers(self, arr, k):
        if k >= len(arr): return arr
        def quick_sort(l, r):
            if l >= r: return
            i, j = l, r
            while i < j:
                while i < j and arr[j] >= arr[l]: j -= 1
                while i < j and arr[i] <= arr[l]: i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[i], arr[l] = arr[l], arr[i]
            if k < i: quick_sort(l, i-1)
            if k > i: quick_sort(i+1, r)
            return arr[:k]
        return quick_sort(0, len(arr)-1)

# 快排第k大
# p = len(arr)-k
# arr[p]代表第n-k+1 小即 第k大。
class Solution4(object):
    def getLeastNumbers(self, arr, k):
        pass

# 堆排序第k小
# 构建k长度的大根堆，小于的插入，遍历完最后堆顶为第k小
class Solution5(object):
    def getLeastNumbers(self, arr, k):
        pass

# 堆排序第k大
# 构建k长度的小跟堆，大于的插入，遍历完最后堆顶为第k大
class Solution6(object):
    def getLeastNumbers(self, arr, k):
        pass

if __name__ == '__main__':
    s = Solution3()
    arr = [4,5,1,6,2,7,3,8,0,2,3,3,2]
    arr2 = [4,5,1,6,2,7,3,8,0,2,3,3,2]
    arr2.sort()
    print arr2
    k = 0
    print(s.getLeastNumbers(arr, k))
    k = 1
    print(s.getLeastNumbers(arr, k))
    k = 2
    print(s.getLeastNumbers(arr, k))
    k = 3
    print(s.getLeastNumbers(arr, k))
    k = 4
    print(s.getLeastNumbers(arr, k))
    k = 5
    print(s.getLeastNumbers(arr, k))
