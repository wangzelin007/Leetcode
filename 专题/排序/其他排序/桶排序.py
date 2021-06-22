# 计数排序的延伸
# 算法步骤
# 设置几个数组作为空桶。
# 从左到右遍历待排序序列，把每个元素都放到对应的桶中。
# 对每个不是空的桶进行排序。
# 依次取出所有桶中的元素放回原序列。
# 时间复杂度依赖数据的分布情况
# 平均时间复杂度O(n+k) 最坏O(n**2 * k)
# 空间复杂度 O(nk)
from ctime import *

def Bucket_Sort(array, bucketsize):
    minValue = min(array)
    maxValue = max(array)
    res = []
    bucketcount = (maxValue - minValue + 1) // bucketsize
    # 空桶
    bucket_lists = [[] for i in range(bucketcount)]
    # 填充桶
    for i in array:
        bucket_index = (i - minValue) // bucketsize
        bucket_lists[bucket_index].append(i)
    # 桶内排序使用快排
    for j in bucket_lists:
        Quick_Sort_2(j, 0, len(j)-1)
    # 依次放回res
    for j in bucket_lists:
        if len(j) != 0:
            res.extend(j)
    return res

import random
def Quick_Sort_2(array, left, right):
    if left >= right:
        return
    random_index = random.randint(left, right)
    pivot = array[random_index]
    array[left], array[random_index] = array[random_index], array[left]

    lt = left  # array[left+1 : lt]  < pivot
    gt = right + 1   # array[gt: right] > pivot
    i = left + 1    # array[lt+1: i] == pivot

    while i < gt:
        if array[i] < pivot:
            array[i], array[lt+1] = array[lt+1], array[i]
            lt += 1
            i += 1
        elif array[i] > pivot:
            array[i], array[gt-1] = array[gt-1], array[i]
            gt -= 1
        else:
            i += 1
    array[left], array[lt] = array[lt], array[left]
    print(array)
    Quick_Sort_2(array, left, lt - 1)
    Quick_Sort_2(array, gt, right)

@cTime
def bucket_sort(li, n=100, max_num=10000):
    buckets = [[] for _ in range(n)]
    for val in li:
        i = min(n-1, val // (max_num // n))
        buckets[i].append(val)
        for j in range(len(buckets[i])-1, 0, -1):
            if buckets[i][j] < buckets[i][j-1]:
                buckets[i][j], buckets[i][j-1] = buckets[i][j-1], buckets[i][j]
            else:
                break

    ans = []
    for buc in buckets:
        ans.extend(buc)
    return ans

import random
li = [random.randint(0,10000) for _ in range(100000)]
li = bucket_sort(li)
print(li)
