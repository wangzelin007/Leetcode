# 给一非空的单词列表，返回前k个出现次数最多的单词。
# 返回的答案应该按单词出现频率由高到低排序。
# 如果不同的单词有相同出现频率，按字母顺序排序。
# 示例 1：
# 输入: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# 输出: ["i", "love"]
# 解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
# 注意，按字母顺序 "i" 在 "love" 之前。
# 示例 2：
# 输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
# 输出: ["the", "is", "sunny", "day"]
# 解析: "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，
# 出现次数依次为 4, 3, 2 和 1 次。
# 注意：
# 假定 k 总为有效值， 1 ≤ k ≤ 集合元素数。
# 输入的单词均由小写字母组成。
# 扩展练习：
# 尝试以O(n log k) 时间复杂度和O(n) 空间复杂度解决。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/top-k-frequent-words
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
import collections
import heapq
from functools import cmp_to_key

class Solution1:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hash = collections.Counter(words)
        res = sorted(hash, key=lambda word:(-hash[word], word))
        return res[:k]

class Word:
    def __init__(self, word, fre):
        self.word = word
        self.fre = fre
    def __lt__(self, other):
        if self.fre != other.fre:
            return self.fre < other.fre
        return self.word > other.word

class Solution2:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = collections.Counter(words)
        heap = []

        for word, fre in cnt.items():
            heapq.heappush(heap, Word(word, fre))
            if len(heap) > k:
                heapq.heappop(heap)

        heap.sort(reverse=True)
        return [x.word for x in heap]

class Solution3:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = collections.Counter(words)

        def cmp(a, b):
            if d[a] > d[b] or (d[a] == d[b] and a < b):
                return -1
            else:
                return 1
        return sorted(d.keys(), key=cmp_to_key(cmp))[:k]

# 同方法1
class Solution4:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = collections.Counter(words)
        tmp = []
        for word, num in d.items():
            tmp.append((num, word))
        ret = sorted(tmp, key=lambda x: (-x[0], x[1]))
        return [i[1] for i in ret[:k]]

