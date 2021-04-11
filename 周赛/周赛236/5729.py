# _*_ coding: utf-8 _*_
class MKAverage(object):

    def __init__(self, m, k):
        """
        :type m: int
        :type k: int
        """
        self.arr = []
        self.m = m
        self.k = k


    def addElement(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.arr.append(num)


    def calculateMKAverage(self):
        """
        :rtype: int
        """
        # 快排都超时了
        # def quickSort(l, r):
        #     if l >= r: return
        #     i, j = l, r
        #     while i < j:
        #         while i < j and tmp[j] >= tmp[l]: j -= 1
        #         while i < j and tmp[i] <= tmp[l]: i += 1
        #         tmp[i], tmp[j] = tmp[j], tmp[i]
        #     tmp[i], tmp[l] = tmp[l], tmp[i]
        #     if self.k < i: quickSort(l, i-1)
        #     if self.k > i: quickSort(i+1, r)
        #     if len(tmp) - self.k < i: quickSort(l, i-1)
        #     if len(tmp) - self.k > i: quickSort(i+1, r)
        #     return tmp[self.k:-self.k]
        if len(self.arr) < self.m: return -1
        else: tmp = self.arr[len(self.arr)-self.m:]
        tmp.sort()
        # tmp = quickSort(0, len(tmp)-1)
        tmp = tmp[self.k:-self.k]
        return sum(tmp)/len(tmp)

if __name__ == '__main__':
    s = MKAverage(6,1)
    s.addElement(3)
    s.addElement(1)
    s.addElement(12)
    s.addElement(5)
    s.addElement(3)
    s.addElement(4)
    print(s.calculateMKAverage())

