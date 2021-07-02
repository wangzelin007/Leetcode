# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 首先求两个结点的最近公共先祖
# dist(p,q) = dist(p,root)+dist(q,root)-2*dist(m,root)
# m 为公共先祖
# todo