# 多关键字排序
# 多次分桶
# 不用每次排序，多次分桶本身就是排序
# 时间复杂度O(kn)
# 空间复杂度O(Kn)
def radix_sort(li):
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

import random
li = list(range(100000))
random.shuffle(li)
radix_sort(li)
print(li)