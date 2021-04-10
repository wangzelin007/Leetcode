# 不断地从后面选一个数，然后插入到前面已经有序的序列里
# 时间复杂度：o(n^2)
# 插入排序
def insert_sort(alist):
    n = len(alist)
    for i in range(1,n):
        while (i>0):
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break
    return alist

# 作者：xiao-xie-shui-bu-xing
# 链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/ge-chong-pai-xu-suan-fa-tu-xie-zong-jie-by-ke-ai-x/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。