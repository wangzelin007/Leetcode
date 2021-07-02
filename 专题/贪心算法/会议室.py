# coding: utf-8
# 一个会议室同一时间只能安排一场会议
# 每场会议都拥有 开始时间 和 结束时间
# 实现一个算法让会议室安排的会议最多
# 按照结束时间安排
# 贪心多出现在笔试中，可以先通过暴力法求解
# 贪心和暴力法做对数器验证
import copy

def bestArrange(programs):
    if not programs or len(programs) == 0:
        return 0
    return process(programs, 0, 0)

def process(programs, done, endtime):
    if len(programs) == 0:
        return done
    maxN = done
    for i in range(len(programs)):
        if programs[i][0] >= endtime:
            next = copy.deepcopy(programs)
            del next[i]
            maxN = max(maxN, process(next, done + 1, programs[i][1]))
    return maxN

def bestArrange2(programs):
    programs = sorted(programs, key=lambda x: x[1])
    # print(programs)
    timeLine, res = 0, 0
    for i in range(len(programs)):
        if timeLine <= programs[i][0]:
            res += 1
            timeLine = programs[i][1]
    return res

from functools import cmp_to_key

def bestArrange3(programs):
    # py2.7
    # programs.sort(cmp=lambda x, y: 1 if x[1] > y[1] else -1)
    # py2 && py3
    def cmp(a, b):
        if a[1] > b[1]: return 1
        elif a[1] < b[1]: return -1
        else: return 0
    programs.sort(key=cmp_to_key(cmp))
    print(programs)

def test():
    programs1 = [[0,5],[1,2],[2,3],[3,4],[5,11],[7,8],[9,13],[9,11],[12,13]]
    programs2 = [[0,12],[13,20],[14,15]]
    # print(bestArrange2(programs1))
    # print(bestArrange2(programs2))
    assert bestArrange(programs1) == bestArrange2(programs1)
    assert bestArrange(programs2) == bestArrange2(programs2)
    bestArrange3(programs1)

if __name__ == '__main__':
    test()