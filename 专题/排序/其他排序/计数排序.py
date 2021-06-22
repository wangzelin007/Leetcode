# 适用于已知范围的有重复数据的排序
# O(N)

def count_sort(li, max_count):
    cnt = [0 for _ in range(max_count+1)]
    for i in li:
        cnt[i] += 1
    li.clear()
    for idx, val in enumerate(cnt):
        for _ in range(val):
            li.append(idx)

import random
li = [random.randint(0, 100) for _ in range(1000)]
print(li)
count_sort(li, 100)
print(li)