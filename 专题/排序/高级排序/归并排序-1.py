# 递归
def merge(li, low, mid, high):
    i = low
    j = mid + 1
    tmp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            tmp.append(li[i])
            i += 1
        else:
            tmp.append(li[j])
            j += 1
    while i <= mid:
        tmp.append(li[i])
        i += 1
    while j <= high:
        tmp.append(li[j])
        j += 1
    li[low:high + 1] = tmp

def merge_sort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid+1, high)
        merge(li, low, mid, high)

# 非递归
def merge_sort2(li, low, high):
    merge_size = 1
    n = len(li)
    while merge_size < n:
        low = 0
        while low < n:
            mid = low + merge_size - 1
            if mid >= n: break
            high = min(mid + merge_size, n - 1)
            merge(li, low, mid, high)
            low = high + 1
        if merge_size > n // 2: break # for java 32 int
        merge_size <<= 1

li = list(range(100))
import random
random.shuffle(li)
print(li)
# merge_sort(li, 0, len(li)-1)
merge_sort2(li, 0, len(li)-1)
print(li)