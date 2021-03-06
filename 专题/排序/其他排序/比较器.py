# coding: utf-8
# topK 问题
from typing import List
import collections
from functools import cmp_to_key
import random

# cmp(a, b)
# return -1 取左 a
# return 1 取右 b
# return 0 相等

# 拼成小的数
def auxComp1(x, y):
    if int(str(x)+str(y)) > int(str(y)+str(x)):
        return 1
    elif int(str(x)+str(y)) < int(str(y)+str(x)):
        return -1
    else:
        return 0

# 拼成大的数
def auxComp2(x, y):
    if int(str(x)+str(y)) > int(str(y)+str(x)):
        return -1
    elif int(str(x)+str(y)) < int(str(y)+str(x)):
        return 1
    else:
        return 0

class Solution:
    def largestNumber1(self, nums):
        # 实现compare 需要 -1 1 0 三种
        # 需要实现降序，所以 > return -1; < return 1
        nums.sort(key=cmp_to_key(auxComp2))
        ans = ''.join([str(num) for num in nums])
        return str(int(ans))

    def largestNumber2(self, nums):
        nums_str = map(str, nums)
        compare = lambda x, y: 1 if x + y < y + x else -1
        nums_str.sort(cmp=compare)
        res = "".join(nums_str)
        if res[0] == "0":
            res = "0"
        return res

# 出现概率高的放前面，概率一样的word小的放前面。
    def topKFrequent1(self, words: List[str], k: int) -> List[str]:
        d = collections.Counter(words)

        def cmp(a, b):
            if d[a] > d[b] or (d[a] == d[b] and a < b):
                return -1
            else:
                return 1
        return sorted(d.keys(), key=cmp_to_key(cmp))[:k]

    def topKFrequent2(self, words: List[str], k: int) -> List[str]:
        d = collections.Counter(words)
        tmp = []
        for word, num in d.items():
            tmp.append((num, word))
        # 评率高的放前面， 相等时word小的放前面；
        ret = sorted(tmp, key=lambda x: (-x[0], x[1]))
        return [i[1] for i in ret[:k]]

# 小跟堆 && 大根堆
def heapTest():
    import heapq
    li = [5,1,4,2,3]
    heapq.heapify(li)
    print(li)
    for i in range(len(li)):
        print(heapq.heappop(li), end="")
    li2 = [5,1,4,2,3]
    li2 = [-i for i in li2]
    heapq.heapify(li2)
    for i in range(len(li2)):
        print(-heapq.heappop(li2), end="")

def gen_str(str_len):
    baseStr = 'abc'
    res = ""
    for i in range(str_len):
        res += baseStr[random.randint(0, 2)]
    return res

def test():
    # 生成任意长度字符串
    word = [gen_str(3) for i in range(30)]
    k = 4
    print(word)
    s = Solution()
    assert s.topKFrequent1(word, k) == s.topKFrequent2(word, k)

if __name__ == '__main__':
    test()


