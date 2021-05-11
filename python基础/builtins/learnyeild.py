# 小结
# 1. 凡是可作用于for循环的对象都是Iterable类型；
# 2. 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 2. 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。


# 可以直接作用于for循环的数据类型有以下几种：
# 一类是集合数据类型，如list、tuple、dict、set、str等；
# 一类是generator 生成器，包括生成器和带yield的generator function。
# 所有作用于 for 循环的对象称为 可迭代对象 iterable
# generator 不仅可以作用于 for 循环，还可以调用 next 方法不断返回下一个值。
# 直到最后抛出 StopIteration 错误，表示无法返回下一个值了。
# 所有被 next() 调用并返回下一个值的对象称为迭代器 iterator

# https://www.liaoxuefeng.com/wiki/1016959663602400/1017323698112640
# https://github.com/michaelliao/learn-python3/blob/master/samples/advance/do_iter.py
from collections.abc import Iterable
from collections.abc import Iterator

def learn1():
    nums = [1,2,3,4,5]
    list1 = [n*n for n in nums]
    generator = (n*n for n in nums)
    print(list1)
    print(generator)

    isinstance([], Iterable) # True
    isinstance((x for x in range(10)), Iterable) # True
    isinstance([], Iterator) # False
    isinstance((x for x in range(10)), Iterator) # True
    # Iterable -> Iterator: iter
    isinstance(iter([]), Iterator) # True

# 为什么list、dict、str等数据类型不是Iterator？
# 因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。
# 可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，
# 所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list之类的数据结构是永远不可能存储全体自然数的。

# 2. 为什么要用generator
# 从时间和空间两个维度对比
import memory_profiler as mem
nums = list(range(10000000))
yi = 100000000
def learn2():
    print(f'前: {mem.memory_usage()}') # 424
    list1 = [n*n*yi for n in nums] # 5s
    print(f'list: {mem.memory_usage()}') # 910
    generator = (n*n*yi for n in nums) # 1.1s
    print(f'gen: {mem.memory_usage()}') # 910

# 3. yield
# yield 类似 return 会返回值，但是不会退出。
def calc(nums):
    res = []
    for n in nums:
        if n % 3 == 0: res.append(3*yi)
        elif n % 5 == 0: res.append(5*yi)
        else: res.append(n*yi)
    return res

def gen(nums):
    for n in nums:
        if n % 3 == 0: yield 3*yi
        elif n % 5 == 0: yield 5*yi
        else: yield n*yi

# 4. yield from

if __name__ == '__main__':
    nums = range(10)
    cal = calc(nums)
    gen = gen(nums)
    for i in cal:
        print(i)
    for i in gen:
        print(i)