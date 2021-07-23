# -*- coding:utf-8 -*-

# @Time    : 2018/11/27 上午8:59

# @Author  : wangzelin

# @Email   : 1064534588@qq.com

# @File    : 开方运算.py

# @Project : python

# @Software: PyCharm

# @Remark  : ...
#pow(3,4)乘方
#math.sqrt(25)开方
#牛顿-拉弗森

def mysqrt1(x, n):
    val = x
    last = 0.0
    while (abs(val - last) > 0.00000001):
        last = val
        val = ((n-1)*val + x / val**(n-1)) / n
    print val
    return val

if __name__ == '__main__':
    mysqrt1(4,2)