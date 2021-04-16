# _*_ coding: utf-8 _*_
# 装饰器实现10秒访问一次
import time

# start = 0
def wrapper1(func):
    # 只有初始化时会进入
    start = 0 # 和 nonlocal 配套
    print ('start',start)
    def inner(*args, **kwargs):
        # global start
        # 正式执行以后每次都是进去inner
        # Python 3.x引入了nonlocal关键字，在闭包内用nonlocal声明变量，就可以让解释器在外层函数中查找变量名。
        # nonlocal关键字修饰变量后，标识该变量是上一级函数中的局部变量。
        nonlocal start
        now = time.time()
        print ('inner start',start)
        if now - start >= 10:
            ref = func(*args, **kwargs)
            start = now
            return ref
        else:
            print(f"访问过于频繁，请于{10-int(now-start)}秒之后再访问")
    return inner

@wrapper1
def func1():
    print("我要打游戏")

# 装饰器实现一次访问五次请求
def wrapper2(func):
    def inner(*args, **kwargs):
        for i in range(5):
            ref = func(*args, **kwargs)
        return ref
    return inner

@wrapper2
def func2():
    print("我要打游戏")

if __name__ == '__main__':
    func1()
    time.sleep(1)
    func1()
    time.sleep(1)
    func1()
    time.sleep(1)
    func1()
    time.sleep(1)
    func1()
    time.sleep(1)
    func1()
    time.sleep(1)
    func1()
    time.sleep(1)
    func1()
    time.sleep(1)
    func1()
    time.sleep(1)
    func1()
    time.sleep(1)
    func1()
    time.sleep(1)
    func1()
    # func2()