# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
# 如果反转后整数超过 32 位的有符号整数的范围[−2**31, 2**31− 1] ，就返回 0。
# 假设环境不允许存储 64 位整数（有符号或无符号）。
# 示例 1：
# 输入：x = 123
# 输出：321
# 示例 2：
# 输入：x = -123
# 输出：-321
# 示例 3：
# 输入：x = 120
# 输出：21
# 示例 4：
# 输入：x = 0
# 输出：0
# 提示：
# -2**31 <= x <= 2**31 - 1
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-integer
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0: return 0
        if x < 0: res = -int(str(-x)[::-1])
        else: res = int(str(x)[::-1])
        return res if  -2**31 <= res <= 2**31-1 else 0

    def reverse_better(self, x: int) -> int:
        y, res = abs(x), 0
        # 则其数值范围为 [−2^31,  2^31 − 1]
        boundry = (1<<31) -1 if x>0 else 1<<31
        while y != 0:
            res = res*10 +y%10
            if res > boundry :
                return 0
            y //=10
        return res if x >0 else -res

class Solution1:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        rev = 0
        while x != 0:
            # INT_MIN 也是一个负数，不能写成 rev < INT_MIN // 10
            if rev < INT_MIN // 10 + 1 or rev > INT_MAX // 10:
                return 0
            digit = x % 10
            # Python3 的取模运算在 x 为负数时也会返回 [0, 9) 以内的结果，因此这里需要进行特殊判断
            if x < 0 and digit > 0:
                digit -= 10

            # 同理，Python3 的整数除法在 x 为负数时会向下（更小的负数）取整，因此不能写成 x //= 10
            x = (x - digit) // 10
            rev = rev * 10 + digit

        return rev

if __name__ == '__main__':
    s = Solution()
    x = 123
    print(s.reverse(x))
    x = -123
    print(s.reverse(x))
    x = 120
    print(s.reverse(x))
    x = 0
    print(s.reverse(x))