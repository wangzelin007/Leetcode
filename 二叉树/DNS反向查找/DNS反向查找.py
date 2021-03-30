# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 字典法
def searchDns(ip,cache):
    return cache.get(ip,'None')

if __name__ == '__main__':
    ips = ['1.1.1.1','2.2.2.2','3.3.3.3']
    names = ['www.a.com','www.b.com','www.c.com']
    cache = dict()
    for i in range(len(ips)):
        cache[ips[i]] = names[i]
    ip = '1.1.1.1'
    print searchDns(ip,cache)
    ip = '1.1.1.2'
    print searchDns(ip,cache)
# 二叉树 最左前缀匹配 以后再看，python 面试手册
