# coding: utf-8
def OddTimesNum(li):
    # 全异或得出 a^b
    xor = 0
    for i in li:
        xor ^= i
    # print(xor)
    # 寻找第一个1
    # java: (a & (~a + 1))
    # 取反再+1 其实就是负数的补码表示？
    # ~ 如果位为0，结果是1，如果位为1，结果是0
    # 0001
    # 1111
    # 0001
    # python: (a & (~a + 1)) == (a & (-a))
    # Python位运算 数字在计算机中是以补码保存的，所以用Python位运算作用在补码上
    # python 负数的补码表示 bin(-2 & 0xffffffff)
    # n & (n - 1) 消除一个1，可以用来计算 1 的个数
    # a = 1,原码 0001, 补码 0001
    # -a = -1,原码 1001, 补码 1111
    # https://blog.csdn.net/u011452172/article/details/78190187
    firstOne = xor & (-xor)
    # print(firstOne)
    # 部分异或得出第一个数
    firstNum = 0
    for i in li:
        if i & firstOne != 0:
            firstNum ^= i
    # 得出第二个数
    return [firstNum, xor ^ firstNum]

# 20210705
def OddTimesNum2(li):
    xor = 0
    for i in li:
        xor ^= i # a ^ b
    firstZero = xor & (-xor)
    first = 0
    for i in li:
        if i & firstZero != 0:
            first ^= i
    return [first, xor ^ first]


def test():
    li = [2, 2, 4, 4, 4, 9, 6, 6, 8, 8, 10, 10, 12, 12]
    # print(OddTimesNum(li))
    assert sorted(OddTimesNum(li)) == sorted(OddTimesNum2(li)) == [4, 9]
    li = [2, 2, -4, -4, -4, -9, 6, 6, 8, 8, 10, 10, 12, 12]
    # print(OddTimesNum(li))
    assert sorted(OddTimesNum(li)) == sorted(OddTimesNum2(li)) == [-9, -4]
    li = [2, 2, 4, 4, 4, -9, 6, 6, 8, 8, 10, 10, 12, 12]
    # print(OddTimesNum(li))
    assert sorted(OddTimesNum(li)) == sorted(OddTimesNum2(li)) == [-9, 4]

if __name__ == '__main__':
    test()