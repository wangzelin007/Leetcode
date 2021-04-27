# 编写一个可以从 1 到 n 输出代表这个数字的字符串的程序，但是：
# 如果这个数字可以被 3 整除，输出 "fizz"。
# 如果这个数字可以被 5 整除，输出"buzz"。
# 如果这个数字可以同时被 3 和 5 整除，输出 "fizzbuzz"。
# 例如，当n = 15，输出：1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13, 14, fizzbuzz。
# 假设有这么一个类：
# class FizzBuzz {
# public FizzBuzz(int n) { ... }              // constructor
# public void fizz(printFizz) { ... }          // only output "fizz"
# public void buzz(printBuzz) { ... }          // only output "buzz"
# public void fizzbuzz(printFizzBuzz) { ... }  // only output "fizzbuzz"
# public void number(printNumber) { ... }      // only output the numbers
# }
# 请你实现一个有四个线程的多线程版FizzBuzz，同一个FizzBuzz实例会被如下四个线程使用：
# 线程A将调用fizz()来判断是否能被 3 整除，如果可以，则输出fizz。
# 线程B将调用buzz()来判断是否能被 5 整除，如果可以，则输出buzz。
# 线程C将调用fizzbuzz()来判断是否同时能被 3 和 5 整除，如果可以，则输出fizzbuzz。
# 线程D将调用number()来实现输出既不能被 3 整除也不能被 5 整除的数字。
# 提示：
# 本题已经提供了打印字符串的相关方法，如 printFizz() 等，具体方法名请参考答题模板中的注释部分。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/fizz-buzz-multithreaded
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from threading import *

def printFizz():
    print('fizz')

def printBuzz():
    print('buzz')

def printFizzBuzz():
    print('fizzbuzz')

def printNumber(i):
    print(i)

# Semaphore
class FizzBuzz1:
    def __init__(self, n: int):
        self.n = n
        self.F = Semaphore(0)
        self.B = Semaphore(0)
        self.FB = Semaphore(0)
        self.N = Semaphore(1)

    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(1, self.n+1):
            if i % 3 == 0 and i % 5 != 0:
                self.F.acquire()
                printFizz()
                self.N.release()

    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n+1):
            if i % 5 == 0 and i % 3 != 0:
                self.B.acquire()
                printBuzz()
                self.N.release()

    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n+1):
            if i % 15 == 0:
                self.FB.acquire()
                printFizzBuzz()
                self.N.release()

    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1):
            self.N.acquire()
            if i % 15 == 0: self.FB.release()
            elif i % 5 == 0: self.B.release()
            elif i % 3 == 0: self.F.release()
            else:
                printNumber(i)
                self.N.release()

# Lock
class FizzBuzz2(object):
    def __init__(self, n: int):
        self.n = n+1
        self.FL = Lock()
        self.BL = Lock()
        self.FBL = Lock()
        self.NL = Lock()
        self.FL.acquire()
        self.BL.acquire()
        self.FBL.acquire()

    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(1, self.n):
            if i % 3 == 0 and i % 5 != 0:
                self.FL.acquire()
                printFizz()
                self.NL.release()

    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n):
            if i % 5 == 0 and i % 3 != 0:
                self.BL.acquire()
                printBuzz()
                self.NL.release()

    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n):
            if i % 15 == 0:
                self.FBL.acquire()
                printFizzBuzz()
                self.NL.release()

    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n):
            self.NL.acquire()
            if i % 15 == 0:
                self.FBL.release()
            elif i % 5 == 0:
                self.BL.release()
            elif i % 3 == 0:
                self.FL.release()
            else:
                printNumber(i)
                self.NL.release()

# 四把锁 + 切换
class FizzBuzz3:
    def __init__(self, n: int):
        self.n = n
        self.curr = 0
        self.lock = [Lock() for _ in range(4)]
        self.lockAll()
        self.switchLock()

    def lockAll(self):
        for i in range(4):
            self.lock[i].acquire()

    def releaseAll(self):
        for i in range(4):
            self.lock[i].release()

    def lockAt(self, i):
        self.lock[i].acquire()

    def releaseAt(self, i):
        self.lock[i].release()

    def switchLock(self):
        self.curr += 1
        if self.curr > self.n:
            self.releaseAll()
            return

        if self.curr % 15 == 0:
            self.lock[2].release()
        elif self.curr % 3 == 0:
            self.lock[0].release()
        elif self.curr % 5 == 0:
            self.lock[1].release()
        else:
            self.lock[3].release()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz) -> None:
        while self.curr <= self.n:
            self.lock[0].acquire()
            if self.curr > self.n:
                continue
            printFizz()
            self.switchLock()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz) -> None:
        while self.curr <= self.n:
            self.lock[1].acquire()
            if self.curr > self.n:
                continue
            printBuzz()
            self.switchLock()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz) -> None:
        while self.curr <= self.n:
            self.lock[2].acquire()
            if self.curr > self.n:
                continue
            printFizzBuzz()
            self.switchLock()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber) -> None:
        while self.curr <= self.n:
            self.lock[3].acquire()
            if self.curr > self.n:
                continue
            printNumber(self.curr)
            self.switchLock()

if __name__ == '__main__':
    n = 30
    # foo = FizzBuzz1(n)
    foo = FizzBuzz2(n)
    # foo = FizzBuzz3(n)
    # for i in range(n):
    Threads = []
    t1 = Thread(target=foo.buzz, args=(printBuzz,))
    t2 = Thread(target=foo.fizz, args=(printFizz,))
    t3 = Thread(target=foo.fizzbuzz, args=(printFizzBuzz,))
    t4 = Thread(target=foo.number, args=(printNumber,))
    t1.setDaemon(True)
    t2.setDaemon(True)
    t3.setDaemon(True)
    t4.setDaemon(True)
    Threads.extend([t1, t2, t3, t4])
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    for t in Threads:
        t.join()