# coding: utf-8
def OddTimesNum(li):
    # 全异或得出 a^b
    xor = 0
    for i in li:
        xor ^= i
    print(xor)
    # 寻找第一个1
    # java: (a ^ (~a + 1))
    # python: (a ^ (a - 1))
    firstOne = xor ^ (xor - 1)
    print(firstOne)
    # 部分异或得出第一个数
    firstNum = 0
    for i in li:
        if i & firstOne != 0:
            firstNum ^= i
    # 得出第二个数
    return [firstNum, xor ^ firstNum]

def test():
    li = [2, 2, 4, 4, 4, 9, 6, 6, 8, 8, 10, 10, 12, 12]
    print(OddTimesNum(li))
    assert sorted(OddTimesNum(li)) == [4, 9]
    li = [2, 2, -4, -4, -4, -9, 6, 6, 8, 8, 10, 10, 12, 12]
    print(OddTimesNum(li))
    assert sorted(OddTimesNum(li)) == [-9, -4]
    li = [2, 2, 4, 4, 4, -9, 6, 6, 8, 8, 10, 10, 12, 12]
    print(OddTimesNum(li))
    assert sorted(OddTimesNum(li)) == [-9, 4]

if __name__ == '__main__':
    test()