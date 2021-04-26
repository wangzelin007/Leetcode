# 我们提供了一个类：
# public class Foo {
#     public void first() { print("first"); }
#     public void second() { print("second"); }
#     public void third() { print("third"); }
# }
# 三个不同的线程 A、B、C 将会共用一个Foo实例。
# 一个将会调用 first() 方法
# 一个将会调用second() 方法
# 还有一个将会调用 third() 方法
# 请设计修改程序，以确保 second() 方法在 first() 方法之后被执行，third() 方法在 second() 方法之后被执行。
# 示例 1:
# 输入: [1,2,3]
# 输出: "firstsecondthird"
# 解释:
# 有三个线程会被异步启动。
# 输入 [1,2,3] 表示线程 A 将会调用 first() 方法，线程 B 将会调用 second() 方法，线程 C 将会调用 third() 方法。
# 正确的输出是 "firstsecondthird"。
# 示例 2:
# 输入: [1,3,2]
# 输出: "firstsecondthird"
# 解释:
# 输入 [1,3,2] 表示线程 A 将会调用 first() 方法，线程 B 将会调用 third() 方法，线程 C 将会调用 second() 方法。
# 正确的输出是 "firstsecondthird"。
# 提示：
# 尽管输入中的数字似乎暗示了顺序，但是我们并不保证线程在操作系统中的调度顺序。
# 你看到的输入格式主要是为了确保测试的全面性。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/print-in-order
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from threading import *
import time

def printFirst():
    print('First')

def printSecond():
    print('Second')

def printThird():
    print('Third')

# acquire and release
# 如果状态是unlocked， 可以调用 acquire() 将状态改为locked
# 如果状态是locked， acquire() 会被block直到另一线程调用 release() 释放锁
# 如果状态是unlocked， 调用 release() 将导致 RuntimError 异常
# 如果状态是locked， 可以调用 release() 将状态改为unlocked
class Foo1:
    def __init__(self):
        self.lockOne = Lock()
        self.lockTwo = Lock()
        self.lockOne.acquire()
        self.lockTwo.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        time.sleep(3)
        printFirst()
        self.lockOne.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        time.sleep(2)
        with self.lockOne:
            printSecond()
            self.lockTwo.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        time.sleep(1)
        with self.lockTwo:
            printThird()

# 笨办法
class Foo2:
    def __init__(self):
        self.t = 0

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.t = 1

    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.t != 1:
            time.sleep(1e-3)
        printSecond()
        self.t = 2

    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.t != 2:
            time.sleep(1e-3)
        printThird()

# condition
# threading模块里的Condition方法，后面五种的方法也都是调用这个模块和使用不同的方法了，
# 方法就是启动wait_for来阻塞每个函数，直到指示self.t为目标值的时候才释放线程，
# with是配合Condition方法常用的语法糖，主要是替代try语句的。
class Foo3:
    def __init__(self):
        self.c = Condition()
        self.t = 0

    def first(self, printFirst: 'Callable[[], None]') -> None:
        self.res(0, printFirst)

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.res(1, printSecond)

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.res(2, printThird)

    def res(self, val: int, func: 'Callable[[], None]') -> None:
        with self.c:
            self.c.wait_for(lambda: val == self.t) # 参数是函数对象，返回时bool类型
            func()
            self.t += 1
            self.c.notify_all() # Wake up all threads waiting on this condition.

# Semaphore信号量
class Foo4:
    def __init__(self):
        # todo 一定要背下来！
        # If it is zero on entry, block, waiting until some other thread has called release() to make it larger than zero.
        self.s1 = Semaphore(0)
        self.s2 = Semaphore(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.s1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.s1.acquire()
        printSecond()
        self.s2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.s2.acquire()
        printThird()

# Event事件
class Foo5:
    def __init__(self):
        self.e1 = Event()
        self.e2 = Event()
        # self.e1.clear() # Reset the internal flag to false.

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.e1.set() # Set the internal flag to true.

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.e1.wait() # Block until the internal flag is true.
        printSecond()
        self.e2.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.e2.wait()
        printThird()

# Barrier栅栏
class Foo6:
    def __init__(self):
        self.b1 = Barrier(2)
        self.b2 = Barrier(2)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.b1.wait() # -1 = 1

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.b1.wait() # -1 = 0
        printSecond()
        self.b2.wait() # -1 = 1

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.b2.wait() # -1 = 0
        printThird()

import queue
# Queue队列
class Foo7:
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.q1.put(0)

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.q1.get() # 自动阻塞,直到有值
        printSecond()
        self.q2.put(0)

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.q2.get() # 自动阻塞,直到有值
        printThird()

# Queue队列2
class Foo8:
    def __init__(self):
        self.q1 = queue.Queue(1)
        self.q2 = queue.Queue(1)
        self.q1.put(0)
        self.q2.put(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.q1.get()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # 对于定长 queue put(0) 变为阻塞动作
        self.q1.put(0)
        printSecond()
        self.q2.get()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # 对于定长 queue put(0) 变为阻塞动作
        self.q2.put(0)
        printThird()

# dict字典 最快，不过 leetcode 不算了
class Foo9:
    def __init__(self):
        self.d = {}

    def first(self, printFirst: 'Callable[[], None]') -> None:
        self.d[0] = printFirst
        self.res()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.d[1] = printSecond
        self.res()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.d[2] = printThird
        self.res()

    def res(self) -> None:
        if len(self.d) == 3:
            self.d[0]()
            self.d[1]()
            self.d[2]()

if __name__ == '__main__':
    threads = []
    # a = Foo1() # 为什么 1 明显比 2 慢
    # a = Foo2()
    # a = Foo3()
    # a = Foo4()
    # a = Foo5()
    # a = Foo6()
    # a = Foo7()
    # a = Foo8()
    a = Foo9()
    # a.first(printFirst)
    # args 里面如何传入函树，其实可以直接传
    # 原因是没有初始化 对象a
    # 直接Foo1.first 会报错 Foo1().first 会卡住
    t3 = Thread(target=a.third, args=(printThird,))
    t1 = Thread(target=a.first, args=(printFirst,))
    t2 = Thread(target=a.second, args=(printSecond,))
    threads.extend([t3, t2, t1])
    for t in threads:
        t.start()
