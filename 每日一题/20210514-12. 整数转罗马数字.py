# coding: utf-8
# 罗马数字包含以下七种字符：I，V，X，L，C，D和M。
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 例如， 罗马数字 2 写做II，即为两个并列的 1。12 写做XII，即为X+II。 27 写做XXVII, 即为XX+V+II。
# 通常情况下，罗马数字中小的数字在大的数字的右边。
# 但也存在特例，例如 4 不写做IIII，而是IV。
# 数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。
# 同样地，数字 9 表示为IX。这个特殊的规则只适用于以下六种情况：
# I可以放在V(5) 和X(10) 的左边，来表示 4 和 9。
# X可以放在L(50) 和C(100) 的左边，来表示 40 和90。
# C可以放在D(500) 和M(1000) 的左边，来表示400 和900。
# 给你一个整数，将其转为罗马数字。
# 示例1:
# 输入:num = 3
# 输出: "III"
# 示例2:
# 输入:num = 4
# 输出: "IV"
# 示例3:
# 输入:num = 9
# 输出: "IX"
# 示例4:
# 输入:num = 58
# 输出: "LVIII"
# 解释: L = 50, V = 5, III = 3.
# 示例5:
# 输入:num = 1994
# 输出: "MCMXCIV"
# 解释: M = 1000, CM = 900, XC = 90, IV = 4.
# 1 <= num <= 3999
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/integer-to-roman
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# python 2.7 OrderDict
from collections import OrderedDict
# python > 3.5 字典才是有序的
class Solution:
    # def intToRoman(self, num: int) -> str:
    def intToRoman(self, num):
        # 使用哈希表，按照从大到小顺序排列
        dic = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        hashmap = OrderedDict(sorted(dic.items(), key=lambda t: t[0], reverse=True))
        # print hashmap
        # hashmap = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        res = ''
        for key in hashmap:
            if num // key != 0:
                count = num // key  # 比如输入3995，count 为 3
                res += hashmap[key] * count
                num %= key
        print(res)
        return res

# 哈希表解法
class Solution2:

    VALUE_SYMBOLS = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    def intToRoman(self, num):
    # def intToRoman(self, num: int) -> str:
        roman = list()
        for value, symbol in Solution.VALUE_SYMBOLS:
            while num >= value:
                num -= value
                roman.append(symbol)
            if num == 0:
                break
        return "".join(roman)

# 字典法
class Solution3:

    THOUSANDS = ["", "M", "MM", "MMM"] # 0000，1000，2000，3000
    HUNDREDS = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"] # 000~900
    TENS = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"] # 00~90
    ONES = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"] # 0~9

    def intToRoman(self, num):
    # def intToRoman(self, num: int) -> str:
        return Solution.THOUSANDS[num // 1000] + \
               Solution.HUNDREDS[num % 1000 // 100] + \
               Solution.TENS[num % 100 // 10] + \
               Solution.ONES[num % 10]

if __name__ == '__main__':
    s = Solution()
    s.intToRoman(3995)
