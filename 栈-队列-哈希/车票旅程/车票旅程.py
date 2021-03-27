# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
import json

def printResult(inputs):
    reverseInputs = dict()
    for k, v in inputs.items():
        reverseInputs[v] = k
    start = list(set(inputs.keys())-set(reverseInputs.keys()))
    start = start[0]
    print start,
    while inputs.get(start):
        end = inputs[start]
        start = end
        print start,


def hanDumps(k):
    # python2 打印 list dict
    return json.dumps(k, encoding='UTF-8', ensure_ascii=False)


if __name__ == '__main__':
    inputs = dict()
    inputs[u"西安"] = u"成都"
    inputs[u"北京"] = u"上海"
    inputs[u"大连"] = u"西安"
    inputs[u"上海"] = u"大连"
    printResult(inputs)