# 在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。
# 请找出那个只出现一次的数字。
# 示例 1：
# 输入：nums = [3,4,3,3]
# 输出：4
# 示例 2：
# 输入：nums = [9,1,7,9,7,9,7]
# 输出：1
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (3*sum(list(set(nums)))-sum(nums))//2

# 方法一看不懂 todo

# 方法二 complete
# 使用 与运算 ，可获取二进制数字 num 的最右一位 n1: n1 = num & i
# 配合 无符号右移操作 ，可获取 num 所有位的值（即 n1~ n32): num = num >> 1
# 记录 二进制中从低位到高位，每一位出现1的次数。
# res 左移统计二进制从高位到低位每一位的值。
# res <<= 1
# res |= counts[31-i] % m (m=3)
# 0xffffffff 0x代表二进制 f代表四个1，即32个1
# return res if counts[31] % m == 0 else ~(res ^ 0xffffffff)
# 最高位为0=res 否则等于 res^32位1 取反
# 负数补码num想要恢复为正常数字，需要进行 ~(num ^ 0xffffffff) 操作
# 解释：（num ^ 0xffffffff 按位取反，~ 整体取反，相当于把32位数字前面的数字全部取反）
# 负数的补码是在其原码的基础上，符号位不变，其余各位取反，最后+1
# python 可以用obxxx表示二进制
# ~x = -x -1
# https://zhuanlan.zhihu.com/p/91967268
# https://zhuanlan.zhihu.com/p/352208284
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = [0] * 32
        for num in nums:
            for j in range(32):
                counts[j] += num & 1
                num >>= 1
        res, m = 0, 3
        # counts 存储从低到高
        # [7, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        counts = [7, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4]
        print(counts)
        for i in range(32):
            print('before', bin(res))
            # 只能左移，右移会丢失
            res <<= 1 # 0 的时候左移没有区别
            print('<<', bin(res))
            res |= counts[31-i] % m
            print('after', bin(res))
        return res if counts[31] % m == 0 else ~(res ^ 0xffffffff)

if __name__ == '__main__':
    s = Solution()
    nums = [9,1,7,9,7,9,7]
    s.singleNumber(nums)