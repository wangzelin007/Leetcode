# 5 个沉默寡言的哲学家围坐在圆桌前，每人面前一盘意面。
# 叉子放在哲学家之间的桌面上。（5 个哲学家，5 根叉子）
# 所有的哲学家都只会在思考和进餐两种行为间交替。
# 哲学家只有同时拿到左边和右边的叉子才能吃到面，而同一根叉子在同一时间只能被一个哲学家使用。
# 每个哲学家吃完面后都需要把叉子放回桌面以供其他哲学家吃面。
# 只要条件允许，哲学家可以拿起左边或者右边的叉子，但在没有同时拿到左右叉子时不能进食。
# 假设面的数量没有限制，哲学家也能随便吃，不需要考虑吃不吃得下。
# 设计一个进餐规则（并行算法）使得每个哲学家都不会挨饿；
# 也就是说，在没有人知道别人什么时候想吃东西或思考的情况下，每个哲学家都可以在吃饭和思考之间一直交替下去。
# 问题描述和图片来自维基百科wikipedia.org
# 哲学家从0 到 4 按 顺时针 编号。
# 请实现函数void wantsToEat(philosopher, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork)：
# philosopher哲学家的编号。
# pickLeftFork和pickRightFork表示拿起左边或右边的叉子。
# eat表示吃面。
# putLeftFork和putRightFork表示放下左边或右边的叉子。
# 由于哲学家不是在吃面就是在想着啥时候吃面，所以思考这个方法没有对应的回调。
# 给你 5 个线程，每个都代表一个哲学家，请你使用类的同一个对象来模拟这个过程。
# 在最后一次调用结束之前，可能会为同一个哲学家多次调用该函数。
# 示例：
# 输入：n = 1
# 输出：[[4,2,1],[4,1,1],[0,1,1],[2,2,1],[2,1,1],[2,0,3],[2,1,2],[2,2,2],[4,0,3],[4,1,2],[0,2,1],[4,2,2],[3,2,1],[3,1,1],[0,0,3],[0,1,2],[0,2,2],[1,2,1],[1,1,1],[3,0,3],[3,1,2],[3,2,2],[1,0,3],[1,1,2],[1,2,2]]
# 解释:
# n 表示每个哲学家需要进餐的次数。
# 输出数组描述了叉子的控制和进餐的调用，它的格式如下：
# output[i] = [a, b, c] (3个整数)
# - a 哲学家编号。
# - b 指定叉子：{1 : 左边, 2 : 右边}.
# - c 指定行为：{1 : 拿起, 2 : 放下, 3 : 吃面}。
# 如 [4,2,1] 表示 4 号哲学家拿起了右边的叉子。
# 提示：
# 1 <= n <= 60
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/the-dining-philosophers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from threading import *
from typing import Callable
# from multiprocessing import Process as Thread

# 奇数编号的哲学家先拿左边叉子
# 偶数编号的哲学家先拿右边叉子
class DiningPhilosophers1:
    def __init__(self):
        self.ForkLocks = [Lock() for _ in range(5)]

    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        # 左右叉子编号
        right_fork = philosopher
        left_fork = (philosopher + 1) % 5
        if philosopher % 2 == 0:
            self.ForkLocks[right_fork].acquire()
            self.ForkLocks[left_fork].acquire()
        else:
            self.ForkLocks[left_fork].acquire()
            self.ForkLocks[right_fork].acquire()
        pickLeftFork()
        pickRightFork()
        eat()
        putLeftFork()
        putRightFork()
        self.ForkLocks[right_fork].release()
        self.ForkLocks[left_fork].release()

# 串行进食
class DiningPhilosophers2:
    def __init__(self):
        self.lock = Lock()

    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        self.lock.acquire()
        pickRightFork()
        pickLeftFork()
        eat()
        putRightFork()
        putLeftFork()
        self.lock.release()

# 限制就餐人数为4， 4个人抢5把叉子，一定有一个人吃到并释放掉
class DiningPhilosophers3():
    def __init__(self):
        self.Limit = Semaphore(4)
        self.ForkLocks = [Lock() for _ in range(5)]

    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]', # 输入 和 返回
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:

        right_fork = philosopher
        left_fork = (philosopher + 1) % 5

        self.Limit.acquire()
        self.ForkLocks[right_fork].acquire()
        self.ForkLocks[left_fork].acquire()

        pickLeftFork()
        pickRightFork()
        eat()
        putLeftFork()
        putRightFork()

        self.ForkLocks[left_fork].release()
        self.ForkLocks[right_fork].release()
        self.Limit.release()


# 尝试去拿自己另外一边的叉子，那不到就把自己拿到的一把也释放掉
philosopher = -1

class DiningPhilosophers4():
    """
    output[i] = [a, b, c]
    a 哲学家编号
    b 叉子 1 左边 2 右边
    c 行为 1 拿起 2 放下 3 吃面
    """
    def __init__(self):
        self.f = [Lock() for _ in range(5)]

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        while True:
            if self.f[philosopher].acquire(timeout=0.001): # 通过 timeout 切换 if else
                if philosopher != 4:
                    if self.f[philosopher+1].acquire(timeout=0.001):
                        pickLeftFork(philosopher)
                        pickRightFork(philosopher)
                    else:
                        self.f[philosopher].release()
                        continue
                else:
                    if self.f[0].acquire(timeout=0.001):
                        pickLeftFork(philosopher)
                        pickRightFork(philosopher)
                    else:
                        self.f[philosopher].release()
                        continue
            else:
                continue
            eat(philosopher)
            putLeftFork(philosopher)
            self.f[philosopher].release()
            putRightFork(philosopher)
            if philosopher != 4:
                self.f[philosopher+1].release()
            else:
                self.f[0].release()
            break

list = []

# todo 如何做到像 leetcode 一样不传参调用
def pickLeftFork(philosopher):
    list.append([philosopher, 1, 1])

def pickRightFork(philosopher):
    list.append([philosopher, 2, 1])

def eat(philosopher):
    list.append([philosopher, 0, 3])

def putLeftFork(philosopher):
    list.append([philosopher, 1, 2])

def putRightFork(philosopher):
    list.append([philosopher, 2, 2])

if __name__ == '__main__':
    foo = DiningPhilosophers2()
    threads = []
    for i in range(1):
        thread0 = Thread(target=foo.wantsToEat, args=(0, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork))
        thread1 = Thread(target=foo.wantsToEat, args=(1, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork))
        thread2 = Thread(target=foo.wantsToEat, args=(2, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork))
        thread3 = Thread(target=foo.wantsToEat, args=(3, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork))
        thread4 = Thread(target=foo.wantsToEat, args=(4, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork))
        threads.extend([thread0, thread1, thread2, thread3, thread4])
        thread0.setDaemon(True)
        thread1.setDaemon(True)
        thread2.setDaemon(True)
        thread3.setDaemon(True)
        thread4.setDaemon(True)

        thread0.start()
        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        for t in threads:
            t.join()
    print(list)
    print(len(list))