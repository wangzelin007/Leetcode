# 现在有两种线程，氧 oxygen 和氢 hydrogen，你的目标是组织这两种线程来产生水分子。
# 存在一个屏障（barrier）使得每个线程必须等候直到一个完整水分子能够被产生出来。
# 氢和氧线程会被分别给予 releaseHydrogen 和 releaseOxygen 方法来允许它们突破屏障。
# 这些线程应该三三成组突破屏障并能立即组合产生一个水分子。
# 你必须保证产生一个水分子所需线程的结合必须发生在下一个水分子产生之前。
# 换句话说:
# 如果一个氧线程到达屏障时没有氢线程到达，它必须等候直到两个氢线程到达。
# 如果一个氢线程到达屏障时没有其它线程到达，它必须等候直到一个氧线程和另一个氢线程到达。
# 书写满足这些限制条件的氢、氧线程同步代码。
# 示例 1:
# 输入: "HOH"
# 输出: "HHO"
# 解释: "HOH" 和 "OHH" 依然都是有效解。
# 示例 2:
# 输入: "OOHHHH"
# 输出: "HHOHHO"
# 解释: "HOHHHO", "OHHHHO", "HHOHOH", "HOHHOH", "OHHHOH", "HHOOHH", "HOHOHH" 和 "OHHOHH" 依然都是有效解。
# 提示：
# 输入字符串的总长将会是 3n, 1 ≤n≤ 50；
# 输入字符串中的 “H” 总数将会是 2n 。
# 输入字符串中的 “O” 总数将会是 n 。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/building-h2o
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
def releaseHydrogen():
    print('H')

def releaseOxygen():
    print('O')

from collections import *
from threading import *

# deque 都推荐这个，淡化了竞争，效率更高
class H2O1:
    def __init__(self):
        self.h = deque()
        self.o = deque()

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h.append(releaseHydrogen)
        self.res()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o.append(releaseOxygen)
        self.res()

    def res(self):
        if len(self.h) > 1 and len(self.o) > 0:
            self.h.pop()()
            self.h.pop()()
            self.o.pop()()

# 阻塞队列
from queue import Queue
class H2O1plus:
    def __init__(self):
        self.h = Queue(2)
        self.o = Queue(1)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h.put(releaseHydrogen)
        self.res()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o.put(releaseOxygen)
        self.res()

    def res(self):
        if self.h.full() and self.o.full():
            self.h.get()()
            self.h.get()()
            self.o.get()()

# Semaphore
class H2O2:
    def __init__(self):
        self.h = Semaphore(2)
        self.o = Semaphore(0)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h.acquire()
        releaseHydrogen()
        if self.h._value == 0:
            self.o.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o.acquire()
        releaseOxygen()
        self.h.release()
        self.h.release()

import time # 还要通过 time.sleep 控制切换？
# Lock 这种对比 Semaphore 需要自己维护两个变量 H 和 O 的数量
class H2O3:
    def __init__(self):
        self.h = 0
        self.o = 0
        self.h_lock = Lock()
        self.o_lock = Lock()
        self.t = Thread(target=self.h2o, args=())
        self.t.setDaemon(True)
        self.t.start()

    def h2o(self):
        while True:
            if self.h == 2 and self.o == 1:
                self.h = 0
                self.o = 0
            time.sleep(1e-3)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h_lock.acquire() # 避免连续打出H
        while self.h >= 2:
            time.sleep(1e-3)
        releaseHydrogen()
        self.h += 1
        self.h_lock.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o_lock.acquire() # 避免连续打出O
        while self.o >= 1:
            time.sleep(1e-3)
        releaseOxygen()
        self.o += 1
        self.o_lock.release()

if __name__ == '__main__':
    # foo = H2O1()
    foo = H2O1plus()
    # foo = H2O2()
    # foo = H2O3()
    name = list('OOHHHH')
    print(name)
    threads = []
    for i in name:
        t_name = 'thread' + i
        if i == 'H':
            t_name = Thread(target=foo.hydrogen, args=(releaseHydrogen,))
            threads.append(t_name)
            t_name.setDaemon(True)
            t_name.start()
        else:
            t_name = Thread(target=foo.oxygen, args=(releaseOxygen,))
            threads.append(t_name)
            t_name.setDaemon(True)
            t_name.start()
    for t in threads:
        t.join()
