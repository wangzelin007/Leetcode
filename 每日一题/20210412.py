# _*_ coding: utf-8 _*_
# 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
# 注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
#
# 示例 1：
# 输入：nums = [10,2]
# 输出："210"
# 示例2：
# 输入：nums = [3,30,34,5,9]
# 输出："9534330"
# 示例 3：
# 输入：nums = [1]
# 输出："1"
# 示例 4：
# 输入：nums = [10]
# 输出："10"
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/largest-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from functools import cmp_to_key

def auxComp(x, y):
    if int(str(x)+str(y)) > int(str(y)+str(x)):
        return -1
    elif int(str(x)+str(y)) < int(str(y)+str(x)):
        return 1
    else:
        return 0

class Solution:
    def largestNumber(self, nums):
        # 实现compare 需要 -1 1 0 三种，默认的是升序
        # 需要降序所以 x+y < y+x
        nums.sort(key=cmp_to_key(auxComp))
        ans = ''.join([str(num) for num in nums])
        return str(int(ans))

class Solution2(object):
    def largestNumber(self, nums):
        nums_str = map(str, nums)
        compare = lambda x, y: 1 if x + y < y + x else -1
        nums_str.sort(cmp=compare)
        res = "".join(nums_str)
        if res[0] == "0":
            res = "0"
        return res

if __name__ == '__main__':
    nums = [3,30,34,5,9]
    nums = [0,0]
    s = Solution()
    print(s.largestNumber(nums))
