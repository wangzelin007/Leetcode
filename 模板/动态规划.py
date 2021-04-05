# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# https://blog.csdn.net/Matrix_cc/article/details/109584049
# https://leetcode.com/discuss/general-discussion/458695/Dynamic-Programming-Patterns
# https://www.cnblogs.com/liuyicai/p/10182262.html
# https://blog.csdn.net/AivenZhong/article/details/88959875

def example():
    for i in range(1,target+1):
        for j in range(len(ways)):# ways:达到目标的方法个数
            if ways[i] <= i:
                dp[i] = min(dp[i], dp[i - ways[j]] + 代价(cost) / 路径(path) / 总和(sum))
    return dp[target]

