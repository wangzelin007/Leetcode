#_*_ coding:utf-8 _*_
# 大根堆求第K小
# 可以先构造k个元素的大根堆，则堆顶就是最大值。
# 若k之后的元素小于堆顶，则应该插入该堆，从K开始，一直循环遍历完整个数组，则堆顶就是第k小元素

# 堆排序
# 构造堆：从小堆到大堆，先看最后一个非叶子节点，从下往上
# 时间复杂度 ： o(nlogn)
# 堆排序

# 向下调整函数的实现, 此处建立大根堆，可实现数组升序排列
def sift(alist, low, high):
    # 假设只有根节点需要调整，两棵子树都是堆
    i = low
    j = i*2 + 1 #j指向i的左子树
    tmp = alist[i]
    while j <=high:
        if j+1<= high and alist[j] < alist[j+1] #右子树比较大,则指向右子树
            j = j+1
        if alist[j] > tmp:  # 若子树的值比较大，则根节点换成子树，然后向下看一层
            alist[i] = alist[j]
            i = j
            j = i *2 +1
        else:
            alist[i] = tmp # 子树的值小于根节点，则根节点就放在这一层
            break
    else:
        alist[i] = tmp # j越界跳出循环，则把根节点放在叶子节点


def heap_sort(alist):
    # 1、建堆
    # 先找到最后一个不是叶子节点的根节点，为(n-2)//2 (若叶子节点为i，则他的父节点为(i-1)//2 )
    # 再向上循环根节点，从小到大
    n = len(alist)
    for i in range((n-2)//2, -1, -1):
        sift(alist,i,n-1)

    # 2、挨个出数，按升序排列
    for i in range(n-1, -1, -1):
        alist[0], alist[i] = alist[i], alist[0]
        sift(alist, 0, i-1)

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20, 13]
    heap_sort(li)
    print(li)

# 作者：xiao-xie-shui-bu-xing
# 链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/ge-chong-pai-xu-suan-fa-tu-xie-zong-jie-by-ke-ai-x/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。