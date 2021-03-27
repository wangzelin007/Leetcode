# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
class Pair:
    def __init__(self, x, y):
        self.first = x
        self.second = y

def findPairs(arr):
    results = dict()
    i = 0
    n = len(arr)
    while i < n:
        x = arr[i]
        j = i+1
        while j < n:
            y = arr[j]
            sum = x+y
            if sum not in results:
                results[sum] = Pair(x,y)
            else:
                print "({},{})({},{})".format(results[sum].first,results[sum].second,x,y)
                return
            j += 1
        i += 1

if __name__ == '__main__':
    arr = [3,4,7,10,20,9,8]
    findPairs(arr)