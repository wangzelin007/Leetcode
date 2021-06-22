# 一共十二种排序

# 排序1 冒泡排序
# 两两交换每趟确定一个最大值或者最小值
# 时间复杂度O(n2) 空间复杂度O(1) 原地交换
def bubble_sort(li):
    n = len(li)
    for i in range(n-1, 0, -1):
        count = 0
        for j in range(i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                count += 1
        if not count:
            break

# 排序2 插入排序
# 像摸扑克牌一样，每次拿到的牌从最后一个开始两两比较大小，插入到正确的位置
# 每轮插入一张牌，每次插入都要两两比较
# 时间复杂度O(n2) 空间复杂度O(1)
# 为什么空间复杂度O(1)，因为每轮都从无序部分拿第一个数插入到有序部分，可以原地交换
def insert_sort(li):
    n = len(li)
    for i in range(1, n):
        while i > 0:
            if li[i] < li[i-1]:
                li[i], li[i-1] = li[i-1], li[i]
                i -= 1
            else:
                break

# 排序3 选择排序 每一趟选择一个最小值放到最前面
# 时间复杂度O(n2)
def select_sort(li):
    n = len(li)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if li[j] < li[min_idx]:
                min_idx = j
        li[i], li[min_idx] = li[min_idx], li[i]

# 排序4 堆排序
# 1. 调整函数 比较节点和左右孩子
# 2. 构建堆，从最后一个非叶子根节点逆序构建堆
# 3. 交换堆顶元素和最后一个元素 并 调整堆（出数）
def shift(li, low, high):
    i = low
    j = 2 * i + 1
    tmp = li[i]
    while j <= high:
        if j+1 <= high and li[j + 1] > li[j]:
            j = j + 1
        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = i * 2 + 1
        else:
            li[i] = tmp
            break
    # while 条件为 false 才执行
    else:
        li[i] = tmp

def heap_sort_max(li):
    n = len(li)
    for i in range((n-2)//2, -1, -1):
        shift(li, i, n-1)
    # print('heap_create',li)
    for i in range(n-1, -1, -1):
        li[0], li[i] = li[i], li[0]
        shift(li, 0, i-1)

def shift2(li, low, high):
    i = low
    j = i * 2 + 1
    tmp = li[i]
    while j <= high:
        if j + 1 <= high and li[j+1] < li[j]:
            j = j + 1
        if li[j] < tmp:
            li[i] = li[j]
            i = j
            j = i * 2 +1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp

def heap_sort_min(li):
    n = len(li)
    for i in range((n-2) // 2, -1, -1):
        shift2(li, i, n-1)
    for i in range(n-1, -1, -1):
        li[0], li[i] = li[i], li[0]
        shift2(li, 0, i - 1)

def heap_sort_py(li):
    import heapq
    heapq.heapify(li)
    ans = []
    for i in range(len(li)):
        ans.append(heapq.heappop(li))
    return ans

def merge_sort():
    pass

def quick_sort():
    pass

def radix_sort():
    pass

def shell_sort():
    pass

def bucket_sort():
    pass

def count_sort():
    pass

def binary_search():
    pass

def bs_py():
    pass

if __name__ == '__main__':
    import random
    li = [i for i in range(1000)]
    random.shuffle(li)
    print(li)
    # bubble_sort(li)
    # print('bubble_sort', li)
    # insert_sort(li)
    # print('insert_sort', li)
    # select_sort(li)
    # print('select_sort', li)
    # heap_sort_max(li)
    # print('heap_sort_max', li)
    # heap_sort_min(li)
    # print('heap_sort_min', li)
    ans= heap_sort_py(li)
    print('heap_sort_py', ans)