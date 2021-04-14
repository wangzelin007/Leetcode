# _*_ coding: utf-8 _*_
# 拆分到单个元素，然后两个两个往上进行递归合并。设置left 和right两个游标,进行合并。
# 时间复杂度：o(nlogn)
# 归并排序
def merge_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist
    mid = n//2
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])

    left_point,right_point = 0,0
    result = []
    while left_point < len(left) and right_point < len(right):
        if left[left_point] <= right[right_point]:
            result.append(left[left_point])
            left_point += 1
        else:
            result.append(right[right_point])
            right_point += 1

    result += left[left_point:]
    result += right[right_point:]
    return result

if __name__ == '__main__':
    print(merge_sort([5,6,7,1,2,3,4,8]))

# 作者：xiao-xie-shui-bu-xing
# 链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/ge-chong-pai-xu-suan-fa-tu-xie-zong-jie-by-ke-ai-x/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。