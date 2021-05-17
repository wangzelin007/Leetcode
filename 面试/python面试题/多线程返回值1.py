# coding: utf-8
from threading import Thread

class BaseThread(Thread):
    '''封装异步多线程工具'''
    def __init__(self, func, *args, **kwargs):
        super(BaseThread, self).__init__()
        self.func = func
        self._args = args
        self._kwargs = kwargs

    def run(self):
        self.result = self.func(*self._args, **self._kwargs)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None

def sum(s1, s2):
    # IO 操作耗时1秒
    return s1 + s2

def main(a, b, c, d):
    # 求(a+b)*(c+d)
    t1 = BaseThread(sum, a, b)
    t2 = BaseThread(sum, c, d)
    t1.start()
    t2.start()
    x1 = t1.get_result()
    x2 = t2.get_result()
    print(x1 * x2)
    return x1 * x2


if __name__ == '__main__':
    main(1, 2, 3, 4)