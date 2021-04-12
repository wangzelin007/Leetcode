# _*_ coding: utf-8 _*_
# 判断
# num & num-1 = 0

# 非递归
def log2(num):
    i = 0
    while num > 1:
        num >> 1
        i += 1
    return i

# 递归
def log2(num):
    if num == 1:
        return 0
    else:
        return 1 + log2(num >> 1)

# 二进制中1的个数
def count1(num):
    i = 0
    while num:
        num = num & (num-1)
        i += 1
    return i

# A B 二进制位有多少个不相同
# C = A ^ B
# count 1 in C

