# coding: utf-8
class RingQueue:

    def __init__(self, len):
        self.limit = len
        self.len = 0
        self.head = 0
        self.tail = -1
        self.queue = [0 for _ in range(len)]

    def isEmpty(self):
        return self.len == 0

    def size(self):
        return self.len

    def getHead(self):
        if self.isEmpty(): return -1
        else: return self.queue[self.head]

    def getTail(self):
        if self.isEmpty(): return -1
        else: return self.queue[self.tail]

    def enQueue(self, x):
        if self.len < self.limit:
            self.len += 1
            self.tail = self.tail+1 if (self.tail+1) != self.limit else 0
            self.queue[self.tail] = x
        else:
            print("满了")

    def deQueue(self):
        if self.len > 0:
            self.len -= 1
            self.head = self.head+1 if (self.head+1) != self.limit else 0
        else:
            print("空了")

def test():
    q = RingQueue(2)
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)
    q.enQueue(4)
    assert q.getHead() == 1
    assert q.getTail() == 2
    assert q.size() == 2
    q.deQueue()
    q.deQueue()
    q.deQueue()
    q.deQueue()
    assert q.size() == 0
    assert q.isEmpty() == True
    assert q.getHead() == -1
    assert q.getTail() == -1

if __name__ == '__main__':
    test()