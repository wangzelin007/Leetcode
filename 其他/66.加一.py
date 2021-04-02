# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
import math

# 错误解答， pow 谨慎使用！数据过大需要取余 1000000007
# class Solution(object):
#     def plusOne(self, digits):
#         """
#         :type digits: List[int]
#         :rtype: List[int]
#         """
#         n = len(digits)
#         res = 0
#         for i in digits:
#             n -= 1
#             res += int(math.pow(10,n))*i
#         res += 1
#         ls = list()
#         for i in str(res):
#             ls.append(int(i))
#         return ls

# 递归
class Solution:
    def plusOne(self, digits):
        if digits[-1]!=9:
            # 末位不是九
            digits[-1]+=1
            return digits
        else:
            # 末位是九,且可以进位
            if digits[:-1]:
                # 正常情况
                digits=self.plusOne(digits[:-1])
                digits.append(0)
                return digits
            # 末位是九,无法进位
            else:
                # 非正常情况，只有[9]这一种需要进位但是有没有前面的位可以用于进位的情况
                # 返回[1,0]
                return [1,0]

class Solution:
    def plusOne(self, digits):
        for i in range(len(digits)-1,-1,-1):# 左闭右开
            digits[i] += 1
            digits[i] %= 10
            if digits[i]:
                return digits
        digits.insert(0,1)
        return digits

if __name__ == '__main__':
    s = Solution()
    digits = [9,8,9]
    # digits = [7, 2, 8, 5, 0, 9, 1, 2, 9, 5, 3, 6, 6, 7, 3, 2, 8]
    # digits = [7, 2, 8, 5, 0, 9, 1, 2, 9, 5, 3, 6, 6, 7, 3, 2, 8, 4, 3, 7, 9, 5, 7, 7, 4, 7, 4, 9, 4, 7, 0]
    # digits = [7,2,8,5,0,9,1,2,9,5,3,6,6,7,3,2,8,4,3,7,9,5,7,7,4,7,4,9,4,7,0,1,1,1,7,4,0,0,6]
    print(s.plusOne(digits))