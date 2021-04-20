# 实现strStr()函数。
# 给你两个字符串haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。
# 如果不存在，则返回 -1 。
# 说明：
# 当needle是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
# 对于本题而言，当needle是空字符串时我们应当返回 0 。
# 这与 C 语言的strstr()以及 Java 的indexOf()定义相符。
# 示例 1：
# 输入：haystack = "hello", needle = "ll"
# 输出：2
# 示例 2：
# 输入：haystack = "aaaaa", needle = "bba"
# 输出：-1
# 示例 3：
# 输入：haystack = "", needle = ""
# 输出：0
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/implement-strstr
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "": return 0
        if needle not in haystack: return -1
        return haystack.index(needle)

# KMP todo
class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        s = haystack        #纯粹为了好写
        t = needle
        ############ 方法1：BF
        sn, tn = len(s), len(t)
        if tn == 0:
            return 0
        i, j = 0, 0
        while i < sn and j < tn:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i = i - j + 1   #回退
                j = 0
        ## j指针遍历了t
        if j == tn:
            return i - j
        return -1

# Sunday todo
# https://leetcode-cn.com/problems/implement-strstr/solution/python3-sundayjie-fa-9996-by-tes/
class Solution3:
    def strStr(self, haystack: str, needle: str) -> int:

        # Func: 计算偏移表
        def calShiftMat(st):
            dic = {}
            for i in range(len(st)-1,-1,-1):
                if not dic.get(st[i]):
                    dic[st[i]] = len(st)-i
            dic["ot"] = len(st)+1
            return dic

        # 其他情况判断
        if len(needle) > len(haystack):return -1
        if needle=="": return 0

        # 偏移表预处理
        dic = calShiftMat(needle)
        idx = 0

        while idx+len(needle) <= len(haystack):

            # 待匹配字符串
            str_cut = haystack[idx:idx+len(needle)]

            # 判断是否匹配
            if str_cut==needle:
                return idx
            else:
                # 边界处理
                if idx+len(needle) >= len(haystack):
                    return -1
                # 不匹配情况下，根据下一个字符的偏移，移动idx
                cur_c = haystack[idx+len(needle)]
                if dic.get(cur_c):
                    idx += dic[cur_c]
                else:
                    idx += dic["ot"]


        return -1 if idx+len(needle) >= len(haystack) else idx

# Rabin-Karp todo
# https://leetcode-cn.com/problems/implement-strstr/solution/28-shi-xian-strstrbf-rk-kmpsan-jie-fa-py-wodj/
class Solution4:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        if n > m: return -1
        def char_to_int(c):
            return ord(c) - ord('a')

        a = 26
        modulus = 2 ** 31

        hash_h = 0
        hash_n = 0

        for i in range(n):
            hash_h = (hash_h * a + char_to_int(haystack[i])) % modulus
            hash_n = (hash_n * a + char_to_int(needle[i])) % modulus
        if hash_h == hash_n and haystack[:n] == needle:
            return 0

        # 长度为n的滑动窗口，第一个数的幂次为a ^ (n - 1) = b
        b = pow(a, n - 1, modulus)
        for i in range(n, m):
            hash_h = ((hash_h - char_to_int(haystack[i - n]) * b) * a + char_to_int(haystack[i])) % modulus
            if hash_h == hash_n and haystack[i - n + 1: i + 1] == needle:
                return i - n + 1
        return -1

# 双指针
# 链接：https://leetcode-cn.com/problems/implement-strstr/solution/28shi-xian-strstr-biao-zhun-de-shuang-zh-4y54/
class Solution5:
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        left = 0
        right = len(needle)
        while right <= len(haystack):
            if haystack[left:right] == needle:
                return left
            left += 1
            right += 1
        return -1

# Boyer-Moore todo
# https://leetcode-cn.com/problems/implement-strstr/solution/zhe-ke-neng-shi-quan-wang-zui-xi-de-kmp-8zl57/
# https://leetcode-cn.com/problems/implement-strstr/solution/28-shi-xian-strstr-pythonjie-ti-si-lu-by-wrallen/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle and not haystack: return -1
        if not needle: return 0
        nee_len = len(needle)
        # 文本串 开始的下标
        hay_end_index = nee_len - 1
        # 当文本串的下标没有到结尾
        while hay_end_index < len(haystack):
            tem_hay = hay_end_index
            tem_nee = nee_len - 1
            while haystack[tem_hay] == needle[tem_nee]:
                tem_hay -= 1
                tem_nee -= 1
                if tem_nee < 0:
                    return hay_end_index - nee_len + 1
            bad_move = tem_nee - self.findIndex(needle[0:tem_nee], haystack[tem_hay])
            # god_move = 代码需要补充
            hay_end_index = bad_move
        return -1

    # 获取该字符最近的下标
    def findIndex(self, new_needle, char):
        index = -1
        for i in range(len(new_needle)):
            if new_needle[i] == char: index = i
        return index
