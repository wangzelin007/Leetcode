# 主要集中在加载到缓存中
# 循环的差别不会太大

import time
arr = [i for i in range(100000)]
start = time.time()
for i in range(0, 100000):
    arr[i] *= 3
print(time.time() - start)
for i in range(0, 100000, 16):
    arr[i] *= 3
print(time.time() - start)