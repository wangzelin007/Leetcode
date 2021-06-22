# 是否可以被分解为两个质数
# 遍历
def isPrime1(n):
    if n <= 3: return n > 1
    for i in range(2, n):
        if n % i == 0: return False
    return True

# 遍历到sqrt
def isPrime2(n):
    if n <=3: return n > 1
    for i in range(2, n**0.5):
        if n % i == 0: return False
    return True

# https://www.zhihu.com/question/51188614
# 6x+1 和 6x-1
import math     # 使用 math 模块来开平方
num = 100000
s = 1  # 默认考虑（3，5）
def f1(n):
    if n == 5 or n == 7:
        return True
    elif n % 5 == 0 and n % 7 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 1):   # 这里 +1是将开方后的结果包含在内。
            if n % i == 0:
                return False
        return True


for i in range(5, num+1, 6):
    if f1(i) and f1(i+2) and (i+2)<=num:  # 最后的条件是限制素数对超过N
        s += 1
#         print((i,i+2),s)
print(s)

if __name__ == '__main__':
    print(isPrime1(5))
    print(isPrime1(6))
    # 如何判断15 27 这种呢？