# 166. Fraction to Recurring Decimal
# Given two integers representing 代表 the numerator 分子 and denominator 分母 of a fraction 分数,
# return the fraction in string format.
# If the fractional part is repeating, enclose the repeating part in parentheses 括号.
# If multiple answers are possible, return any of them.
# It is guaranteed 保证 that the length of the answer string is less than 104 for all the given inputs.
#
# Example 1:
# Input: numerator = 1, denominator = 2
# Output: "0.5"
# Example 2:
# Input: numerator = 2, denominator = 1
# Output: "2"
# Example 3:
# Input: numerator = 2, denominator = 3
# Output: "0.(6)"
# Example 4:
# Input: numerator = 4, denominator = 333
# Output: "0.(012)"
# Example 5:
# Input: numerator = 1, denominator = 5
# Output: "0.2"
#
# Constraints:
# -2**31 <= numerator, denominator <= 2**31 - 1
# denominator != 0


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)

        s = []
        if (numerator < 0) != (denominator < 0):
            s.append('-')

        numerator = abs(numerator)
        denominator = abs(denominator)
        integerPart = numerator // denominator
        s.append(str(integerPart))
        s.append('.')

        indexMap = {}
        remainder = numerator % denominator
        while remainder and remainder not in indexMap:
            indexMap[remainder] = len(s)
            remainder *= 10
            s.append(str(remainder // denominator))
            remainder %= denominator
        if remainder:
            insertIndex = indexMap[remainder]
            s.insert(insertIndex, '(')
            s.append(')')

        return ''.join(s)

def test():
    s = Solution()
    assert s.fractionToDecimal(1, 2) == "0.5"
    assert s.fractionToDecimal(2, 1) == "2"
    assert s.fractionToDecimal(2, 3) == "0.(6)"
    assert s.fractionToDecimal(4, 333) == "0.(012)"
    assert s.fractionToDecimal(1, 5) == "0.2"

if __name__ == '__main__':
    test()