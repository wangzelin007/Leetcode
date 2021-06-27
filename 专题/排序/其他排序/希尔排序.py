# 希尔排序: 插入排序的延伸
# 是一种分组插入排序算法
# 时间复杂度：o(nlogn) ~ o(n^2)
# 逐渐缩小gap，宏观调控
def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            j = i
            while j > 0:
                if alist[j] < alist[j-gap]:
                    alist[j], alist[j-gap] = alist[j-gap], alist[j]
                    j -= gap
                else:
                    break
        gap //= 2
    return alist

def test():
    import random
    alist = [random.randint(0,100) for _ in range(100)]
    print(alist)
    shell_sort(alist)
    print(alist)

if __name__ == '__main__':
    test()

# 作者：xiao-xie-shui-bu-xing
# 链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/ge-chong-pai-xu-suan-fa-tu-xie-zong-jie-by-ke-ai-x/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。