# 5 = 2 + 3 yes
# 12 = 3 + 4 + 5 yes
# 2 = 1 + 1 no
# 给定一个数N，返回N是否可以表示成若干连续正数的和
def isNum(n):
    for i in range(1,n):
        sums = i
        j = i + 1
        while j <= n:
            if sums + j > n: break
            if sums + j == n: return True
            sums += j
            j += 1
    return False

# n < 3 False
# n > 3 时，2的次幂返回False
# n & (n - 1) == 0 2的次幂
# n & (n - 1) != 0 不是2的次幂
def isNum2(n):
    if n < 3: return False
    return False if n & (n - 1) == 0 else True

def test():
    for i in range(100):
        # print("{}: {}".format(i, isNum(i)))
        assert isNum(i) == isNum2(i)

if __name__ == '__main__':
    test()