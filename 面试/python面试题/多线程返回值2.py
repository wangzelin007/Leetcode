# coding: utf-8
from threading import Thread
from collections import deque

q = deque()
# list 自己是线程安全的，所以 list.pop()，list.append()，len(list) 等都是线程安全的；
# list 里面的数据不一定是线程安全的，比如 list[0] += 1 就不是线程安全的，
# 这是因为 v += 1 本身就不是原子的，这和 list 无关，反之如果 v += 1 是原子的，那么 list[0] += 1 也是线程安全的；

class BaseThread(Thread):
    '''封装异步多线程工具'''
    def __init__(self, func, *args, **kwargs):
        super(BaseThread, self).__init__()
        self.func = func
        self._args = args
        self._kwargs = kwargs

    def run(self):
        q.append(self.func(*self._args, **self._kwargs))

def sum(s1, s2):
    # IO 操作耗时1秒
    return s1 + s2

def main(a, b, c, d):
    # 求(a+b)*(c+d)
    t1 = BaseThread(sum, a, b)
    t2 = BaseThread(sum, c, d)
    t1.start()
    t2.start()
    ans = reduce(lambda x, y: x*y, q)
    print(ans)
    return ans


if __name__ == '__main__':
    main(1, 2, 3, 4)