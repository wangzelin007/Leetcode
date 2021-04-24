# 写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。
# 示例:
# 输入: a = 1, b = 1
# 输出: 2
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/solution/mian-shi-ti-65-bu-yong-jia-jian-cheng-chu-zuo-ji-7/
# Python 负数的存储：
# Python，Java 等语言中的数字都是以 补码 形式存储的。
# 但 Python 没有 int , long 等不同长度变量，即在编程时无变量位数的概念。
# 获取负数的补码： 需要将数字与十六进制数 0xffffffff 相与。
# 可理解为舍去此数字 32 位以上的数字（将 32 位以上都变为 00 ），从无限长度变为一个 32 位整数。
# 返回前数字还原： 若补码 aa 为负数（ 0x7fffffff 是最大的正数的补码 ），需执行 ~(a ^ x) 操作，将补码还原至 Python 的存储格式。
# a ^ x 运算将 1 至 32 位按位取反； ~ 运算是将整个数字取反；因此， ~(a ^ x) 是将 32 位以上的位取反，1 至 32 位不变。
# print(hex(1)) # = 0x1 补码
# print(hex(-1)) # = -0x1 负号 + 原码 （ Python 特色，Java 会直接输出补码）
# print(hex(1 & 0xffffffff)) # = 0x1 正数补码
# print(hex(-1 & 0xffffffff)) # = 0xffffffff 负数补码
# print(-1 & 0xffffffff) # = 4294967295 （ Python 将其认为正数）


class Solution:
    def __init__(self):
        self.x = 0xffffffff

    def add(self, a: int, b: int) -> int:
        x = 0xffffffff # 4294967295 全1
        # 注意啦这个地方非常容易忘记！！！
        # 注意啦这个地方非常容易忘记！！！
        # 注意啦这个地方非常容易忘记！！！
        a, b = a & x, b & x # 正数本身，负数补码
        while b != 0:
            print('a',a,'b',b)
            a, b = (a ^ b), (a & b) << 1 & x # a ^ b
            # a, b = (a ^ b), (a & b) << 1
            # 如果去掉 & x ,
            # 我们可以看到在例二 python 会继续累加
            # a 2147483648 b 2147483648
            # a 0 b 4294967296
            # result2 -8589934592
            # 我们可以看到在例三 python 也会继续累加
            # a 4294967293 b 4294967293
            # a 0 b 8589934586
            # result3 -4294967302
        # print(a)
        return a if a <= 0x7fffffff else ~(a ^ x) # <=2147483647 0111全1 即正数

    def func1(self, a: int, b: int) -> int:
        print(a & self.x) # 3 正数是本身
        print(b & self.x) # 4294967293 负数是补码 ~(补码^0xffffffff) 还原

    def func2(self, a: int, b: int) -> int:
        c = a&b # 3&-3
        d = a&(b&self.x)
        print('c',c) # 1
        print('d',d)
        print(c<<1) # 2 左移：向高位移动，以左为尊，不足补零。
        print(c>>1) # 0 右移：向低位移动，移到符号右边的忽略。

    def func3(self, a: int, b: int) -> int:
        print(~(a^self.x)) # -4294967293 正数不适用
        print(~(b^self.x)) # 4294967293 补码
        print(~(~(b^self.x))^self.x) # -3

if __name__ == '__main__':
    s = Solution()
    print('result1',s.add(1,1))
    print('result2',s.add(3,-3))
    print('result3',s.add(-3,-3))
    # s.func1(3,-3)
    # s.func2(3,-3)
    # s.func3(3,-3)

