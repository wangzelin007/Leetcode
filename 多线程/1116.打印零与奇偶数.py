# 假设有这么一个类：
# class ZeroEvenOdd {
# public ZeroEvenOdd(int n) { ... }     // 构造函数
# public void zero(printNumber) { ... }  // 仅打印出 0
# public void even(printNumber) { ... }  // 仅打印出 偶数
# public void odd(printNumber) { ... }   // 仅打印出 奇数
# }
# 相同的一个ZeroEvenOdd类实例将会传递给三个不同的线程：
# 线程 A 将调用zero()，它只输出 0 。
# 线程 B 将调用even()，它只输出偶数。
# 线程 C 将调用odd()，它只输出奇数。
# 每个线程都有一个printNumber 方法来输出一个整数。
# 请修改给出的代码以输出整数序列010203040506... ，其中序列的长度必须为 2n。
# 示例 1：
# 输入：n = 2
# 输出："0102"
# 说明：三条线程异步执行，其中一个调用 zero()，另一个线程调用 even()，最后一个线程调用odd()。
# 正确的输出为 "0102"。
# 示例 2：
# 输入：n = 5
# 输出："0102030405"
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/print-zero-even-odd
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

def printNumber(x):
    print(x)

from threading import *

# 信号量Semaphore * 3
class ZeroEvenOdd1:
    def __init__(self, n):
        self.n = n
        self.zs = Semaphore(1)
        self.es = Semaphore(0)
        self.os = Semaphore(0)

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1):
            self.zs.acquire()
            printNumber(0)
            if i % 2 == 1:
                self.os.release()
            else:
                self.es.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n+1, 2):
            self.es.acquire()
            printNumber(i)
            self.zs.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1, 2):
            self.os.acquire()
            printNumber(i)
            self.zs.release()

# 1优化版 太优美了
class ZeroEvenOdd1plus:
    s = [Semaphore(0), Semaphore(0), Semaphore(1)] # odd, even, zero
    def __init__(self, n):
        self.n = n

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            self.s[2].acquire()
            printNumber(0)
            self.s[i%2].release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1, 2):
            self.s[0].acquire()
            printNumber(i)
            self.s[2].release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n+1, 2):
            self.s[1].acquire()
            printNumber(i)
            self.s[2].release()

# Lock
class ZeroEvenOdd2:
    def __init__(self, n):
        self.n = n

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        pass

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        pass

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        pass
# Event
class ZeroEvenOdd3:
    def __init__(self, n):
        self.n = n

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        pass

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        pass

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        pass
# queue
class ZeroEvenOdd4:
    def __init__(self, n):
        self.n = n

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        pass

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        pass

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        pass
# Event + Semaphore + Lock
class ZeroEvenOdd5:
    def __init__(self, n):
        self.n = n

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        pass

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        pass

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        pass

if __name__ == '__main__':
    n = 5
    # foo = ZeroEvenOdd1(n)
    foo = ZeroEvenOdd1plus(n)
    from threading import *
    theardA = Thread(target=foo.zero, args=(printNumber,))
    theardB = Thread(target=foo.even, args=(printNumber,))
    theardC = Thread(target=foo.odd, args=(printNumber,))
    theards = [theardA, theardB, theardC]
    theardA.setDaemon(True)
    theardB.setDaemon(True)
    theardC.setDaemon(True)
    theardA.start()
    theardB.start()
    theardC.start()
    for t in theards:
        t.join()