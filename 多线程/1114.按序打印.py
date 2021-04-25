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

# 如果状态是unlocked， 可以调用 acquire() 将状态改为locked
# 如果状态是locked， acquire() 会被block直到另一线程调用 release() 释放锁
# 如果状态是unlocked， 调用 release() 将导致 RuntimError 异常
# 如果状态是locked， 可以调用 release() 将状态改为unlocked

from threading import Lock, Thread
import time

def printFirst():
    print('First')

def printSecond():
    print('Second')

def printThird():
    print('Third')

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

if __name__ == '__main__':
    threads = []
    a = Foo1()
    # todo args 里面如何传入函数
    t3 = Thread(target=Foo1.third, kargs={"printFirst": printFirst})
    t1 = Thread(target=Foo1.first, args=())
    t2 = Thread(target=Foo1.second, args=())
    threads.extend([t3, t2, t1])
    for t in threads:
        t.start()













# import queue
#
# class Foo(object):
#     def __init__(self):
#         self.q = queue.Queue(1)
#         self.r = queue.Queue(1)
#
#     def first(self):
#         """
#         :type printFirst: method
#         :rtype: void
#         """
#         # printFirst() outputs "first". Do not change or remove this line.
#         print('First')
#         self.q.put(0)
#
#     def second(self):
#         """
#         :type printSecond: method
#         :rtype: void
#         """
#         self.q.get()
#         # printSecond() outputs "second". Do not change or remove this line.
#         print('Second')
#         self.r.put(0)
#
#     def third(self):
#         """
#         :type printThird: method
#         :rtype: void
#         """
#         self.r.get()
#         # printThird() outputs "third". Do not change or remove this line.
#         print('Third')
#
#
# if __name__ == '__main__':
#     foo = Foo()
#     myDict = {"A": foo.first,
#               "B": foo.second,
#               "C": foo.third}
#     from random import sample
#     myList = sample(['A', 'B', 'C'], k=3)
#     import threading
#     threads = []
#     for i in myList:
#         t_name = 'thread' + i
#         t_name = threading.Thread(target=myDict[i], args=())
#         threads.append(t_name)
#         t_name.setDaemon(True)
#         t_name.start()
#     for t in threads:
#         t.join()

