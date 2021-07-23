# coding: utf-8
# 1.  一行代码实现对列表a中的偶数位置的元素进行加3后求和？
# 比如 a = [1, 2, 3, 4, 5]， 求和结果为 24
# a = [1, 2, 3, 4, 5]
# assert sum([i if idx & 1 == 1 else i+3  for idx,i in enumerate(a)]) == 24

# 2.  请写出执⾏如下脚本后在控制台输出的内容:
# import copy
# a = [[1, 2, 3], [4, 5, 6]]
# b = a
# c = copy.copy(a)
# a.append(7)
# a[1][2] = 10
# print(b)
# print(c)
# [[1, 2, 3], [4, 5, 10], 7]
# [[1, 2, 3], [4, 5, 10]]

# 3. 实现统计一篇英文文章内每个单词的出现频率，并返回出现频率最高的前10个单词及其出现次数？
# qiuping@smartx.com
import string
import collections

class Word:

    def __init__(self, word, fre):
        self.word = word
        self.fre = fre

    def __lt__(self, other):
        if self.fre != other.fre:
            return self.fre < other.fre
        return self.word > other.word

class Solution:

    def findKthWords(self, words, k):
        '''
        :param words: all words in a capital
        :param k: specify how many words to find
        :return: Kth words
        '''
        cnt = collections.Counter(words)
        print(cnt)
        heap = []
        keys = cnt.keys()
        n = len(keys)
        for i in range(k):
            heap.append(Word(keys[i], cnt[keys[i]]))
        for i in range((k-2)//2, -1, -1):
            self.sift(heap, i, k-1)

        for j in range(k, n):
            if cnt[keys[j]] > heap[0].fre:
                heap[0] = Word(keys[j] ,cnt[keys[j]])
                self.sift(heap, 0, k - 1)

        heap.sort(reverse=True)
        return [(x.word, x.fre) for x in heap]

    def sift(self, arr, low, high):
        i = low
        j = i * 2 + 1
        tmp = arr[i]
        while j <= high:
            if j + 1 <= high and arr[j+1] < arr[j]:
                j = j + 1
            if arr[j] < tmp:
                arr[i] = arr[j]
                i = j
                j = i * 2 + 1
            else:
                arr[i] = tmp
                break
        else:
            arr[i] = tmp

def test():
    import random
    random_arr = [random.choice(string.ascii_lowercase) for _ in range(100000)]
    s = Solution()
    k = 10
    print(s.findKthWords(random_arr, k))

if __name__ == '__main__':
    test()