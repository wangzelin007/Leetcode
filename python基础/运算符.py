# _*_ coding: utf-8 _*_
# https://www.runoob.com/python/python-operators.html
a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
c = 0

c = a & b;        # 12 = 0000 1100
print("1 - c 的值为：", c)

c = a | b;        # 61 = 0011 1101
print ("2 - c 的值为：", c)

c = a ^ b;        # 49 = 0011 0001
print ("3 - c 的值为：", c)

c = ~a;           # -61 = 1100 0011 最高位代表符号
print ("4 - c 的值为：", c)

c = a << 2;       # 240 = 1111 0000
print ("5 - c 的值为：", c)

c = a >> 2;       # 15 = 0000 1111
print ("6 - c 的值为：", c)

# 异或
# http://www.ruanyifeng.com/blog/2021/01/_xor.html
# 补码
# http://www.ruanyifeng.com/blog/2009/08/twos_complement.html
# Y补 = (0xffffffff-Y) + 1 确认
# Y = 0xffffffff-Y补+1 推测？
# 负数补码恢复为正常数字 Y = ~(Y补 ^ 0xffffffff) 确认

# 四位计算机的原理及其实现
# http://www.ruanyifeng.com/blog/2011/03/4-bit_computer.html