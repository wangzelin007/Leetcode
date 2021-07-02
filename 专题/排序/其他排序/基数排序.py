# 多关键字排序
# 多次分桶
# 不用每次排序，多次分桶本身就是排序
# 时间复杂度O(kn)
# 空间复杂度O(Kn)
def radix_sort(li):
    if not li or len(li) < 2: return
    max_num = max(li)
    it = 0
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]
        for var in li:
            # var // 1 % 10 -> var // 10 % 10 -> var // 100 % 10
            digit = (var // 10 ** it) % 10
            buckets[digit].append(var)
        li.clear()
        for buc in buckets:
            li.extend(buc)
        it += 1

def radix_sort2(arr):
    n = len(arr)
    if not arr or n < 2: return
    max_num = max(arr)
    it = 0
    help = [0 for _ in range(n)]
    while 10 ** it <= max_num:
        count = [0 for _ in range(10)]
        for i in range(n):
            j = getDigit(arr[i], it)
            count[j] += 1
        for i in range(1, 10):
            count[i] += count[i-1]
        for i in range(n-1, -1, -1):
            j = getDigit(arr[i], it)
            help[count[j]-1] = arr[i]
            count[j] -= 1
        for i in range(n):
            arr[i] = help[i]
        it += 1

def getDigit(num, it):
    digit = (num // 10 ** it) % 10
    return digit

import random, copy
li = list(range(100))
random.shuffle(li)
li1 = copy.deepcopy(li)
li2 = copy.deepcopy(li)
radix_sort(li1)
radix_sort2(li2)
print(li1)
print(li2)
assert li1 == li2