# 每一趟选出一个最大值，排在最后一个
# 也可以每一趟选出一个最小值，排在最后一个
# 在某一趟中如果 count=0 代表无交换，全部有序。
# 因为冒泡排序每一趟都是两两比较！
# 时间复杂度：o(n^2)
def bubble_sort(alist):
    n = len(alist)
    # 执行 n-1 趟
    for i in range(n-1,0,-1):
        count = 0
        for j in range(i):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
                count += 1
        if count == 0:
            break
    return alist

# 作者：xiao-xie-shui-bu-xing
# 链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/ge-chong-pai-xu-suan-fa-tu-xie-zong-jie-by-ke-ai-x/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。