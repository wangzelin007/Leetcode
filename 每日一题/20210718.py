# 面试题 10.02. 变位词组
# 编写一种方法，对字符串数组进行排序，将所有变位词组合在一起。
# 变位词是指字母相同，但排列不同的字符串。
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
# 输出:
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
# 说明：
# 所有输入均为小写字母。
# 不考虑答案输出的顺序。
from collections import OrderedDict
# OrderedDict 是 按照插入方式排序
from collections import defaultdict
from typing import List

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # res_dict = {}
        res_dict = defaultdict(list)
        for word in strs:
            str_dic = {}
            for s in word:
                str_dic[s] = str_dic.get(s, 0) + 1
            key = ''
            str_dic = OrderedDict(sorted(str_dic.items(), key=lambda x: x[0]))
            for i in str_dic.keys():
                key += i + str(str_dic[i])
            # res_dict.setdefault(key, []).append(word)
            res_dict[key].append(word)
        print(res_dict.values())
        return list(res_dict.values())

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for st in strs:
            # sorted 生成的是列表
            key = "".join(sorted(st))
            mp[key].append(st)

        return list(mp.values())

    def groupAnagrams3(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for st in strs:
            counts = [0] * 26
            for ch in st:
                counts[ord(ch) - ord("a")] += 1
            # 需要将 list 转换成 tuple 才能进行哈希
            mp[tuple(counts)].append(st)

        return list(mp.values())


def test():
    s = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    assert s.groupAnagrams(strs) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    assert s.groupAnagrams2(strs) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    assert s.groupAnagrams3(strs) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

if __name__ == '__main__':
    test()