# _*_ coding: utf-8 _*_
import bisect

class MKAverage(object):

    def __init__(self, m, k):
        self.m = m
        self.k = k
        self.stack = []
        self.s = []


    def addElement(self, num):
        """
        :type num: int
        :rtype: None
        """
        # 反向思维，增加一个self.s 同时执行有序插入
        # popleft stack 到len(m)，同时删除self.s 到len(m)
        self.stack.append(num)
        bisect.insort(self.s, num) # 有序插入
        if len(self.stack) > self.m:
            t = self.stack.pop(0)
            ind = bisect.bisect_left(self.s, t) # 返回插入 t 元素的位置
            self.s.pop(ind) # 删除该元素

    def calculateMKAverage(self):
        """
        :rtype: int
        """
        # print(self.stack,self.s,sum(self.s[self.k:-self.k])/(self.m-2*self.k))
        if len(self.s)<self.m:
            return -1
        return (sum(self.s[self.k:-self.k])/(self.m-2*self.k))

if __name__ == '__main__':
    s = MKAverage(6,1)
    s.addElement(3)
    s.addElement(1)
    s.addElement(12)
    s.addElement(5)
    s.addElement(3)
    s.addElement(4)
    s.addElement(4)
    print(s.calculateMKAverage())