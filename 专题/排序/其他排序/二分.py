# coding: utf-8
def binary_search(arr, target):
    l, r = 0, len(arr)-1
    while l <= r:
        m = (l + r) // 2
        if target > arr[m]:
            l = m + 1
        elif target < arr[m]:
            r = m - 1
        else:
            return m
    return l

# 查找第一个大于等于某个值的位置
def binary_search2(arr, target):
    l, r = 0, len(arr)-1
    first = -1
    while l <= r:
        m = (l + r) // 2
        if target > arr[m]:
            l = m + 1
        elif target <= arr[m]:
            first = m
            r = m - 1
    return first

# 查找最后一个小于等于某个值的位置
def binary_search3(arr, target):
    l, r = 0, len(arr)-1
    last = -1
    while l <= r:
        m = (l + r) // 2
        if target >= arr[m]:
            last = m
            l = m + 1
        elif target < arr[m]:
            r = m - 1
    return last

# 查找等于某个值的范围
def find_range(arr, target):
    l = binary_search2(arr, target)
    r = binary_search2(arr, target+1)
    if l == -1 or l == len(arr) - 1:
        return [-1, -1]
    else:
        return [l, max(l, r-1)]

# 查找局部最小
# 0. 相邻的两个数不相等
# 1. 开头第一个数小于第二个数
# 2. 结尾最后一个数小于倒数第二个数
# 3. 中间某一个数小于两边的数
def binary_search5(arr):
    if not arr: return -1
    if len(arr) == 1 or arr[0] < arr[1]: return 0
    if arr[len(arr)-1] < arr[len(arr)-2]: return len(arr)-1
    l, r = 1, len(arr) - 2
    while l < r:
        m = (l + r) // 2
        if arr[m-1] < arr[m]:
            r = m - 1
        elif arr[m+1] < arr[m]:
            l = m + 1
        else:
            return m
    return l

def test():
    arr = [1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4]
    print(binary_search(arr, 2))
    assert binary_search2(arr, 2) == 4
    assert binary_search3(arr, 2) == 8
    assert find_range(arr, 2) == [4, 8]
    arr = [3,2,1,4,5,6]
    print(binary_search5(arr))

if __name__ == '__main__':
    test()