# _*_ coding: utf-8 _*_
# https://docs.python.org/zh-cn/2.7/library/collections.html
from collections import *

# 1. namedtuple() 创建命名元组子类的工厂函数
Point = namedtuple('Point', ['x', 'y'], verbose=True)
print Point # __repr__() 方法，以 name=value 格式列明了元组内容。
p = Point(11, y=22)
p[0] + p[1] # 33
x, y = p
print x, y # 11, 22
p.x + p.y # 33
print p # Point(x=11, y=22)
# 尤其有用于数据库返回的元组
# EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')
# import csv
# for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "rb"))):
#     print emp.name, emp.title
#
# import sqlite3
# conn = sqlite3.connect('/companydata')
# cursor = conn.cursor()
# cursor.execute('SELECT name, age, title, department, paygrade FROM employees')
# for emp in map(EmployeeRecord._make, cursor.fetchall()):
#     print emp.name, emp.title
# somenamedtuple._make(iterable)
t = [11, 22]
Point._make(t) # Point(x=11, y=22)
# somenamedtuple._asdict()
p = Point(x=11, y=22)
p._asdict() # OrderedDict([('x', 11), ('y', 22)])
p._replace(x=33) # Point(x=33, y=22)
# for partnum, record in inventory.items():
#     inventory[partnum] = record._replace(price=newprices[partnum], timestamp=time.now())
print p._fields # ('x', 'y')
Color = namedtuple('Color', 'red green blue')
Pixel = namedtuple('Pixel', Point._fields + Color._fields)
Pixel(11, 22, 128, 255, 0) # Pixel(x=11, y=22, red=128, green=255, blue=0)
getattr(p, 'x') # 11
d = {'x': 11, 'y': 22}
Point(**d) # Point(x=11, y=22)
class Point(namedtuple('Point', 'x y')):
    __slots__ = ()
    @property
    def hypot(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    def __str__(self):
        return 'Point: x=%6.3f  y=%6.3f  hypot=%6.3f' % (self.x, self.y, self.hypot)

for p in Point(3, 4), Point(14, 5/7.):
    print p
# Point: x= 3.000  y= 4.000  hypot= 5.000
# Point: x=14.000  y= 0.714  hypot=14.018

# 2. deque 类似列表(list)的容器，实现了在两端快速添加(append)和弹出(pop)
# deque 由stack或者queue生成，线程安全，支持双端pop append
# append appendleft pop popleft
d = deque('abc')
d.reverse(); print d# list(reversed(d))
d.extend('def'); print d
d.rotate(1)
d.rotate(-1)
d.clear()
# d.pop() # IndexError: pop from an empty deque
d.extendleft('abc') # deque(['c', 'b', 'a'])
l = ['a', 'b', 'c']
l.pop(1); print l

# 3. Counter 字典的子类，提供了可哈希对象的计数功能
cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
print cnt # Counter({'blue': 3, 'red': 2, 'green': 1})
# init
c = Counter('abc') # Counter({'a': 1, 'c': 1, 'b': 1})
print c
c = Counter({'red': 4, 'blue': 2})
print c
c = Counter(cats=4, dogs=8)
print c
c = Counter(['aaa', 'bbb'])
print c['ccc'] # 0
# del
c['ccc'] = 0
print c
del c['ccc']
print c
# elements() 返回一个迭代器，每个元素重复计数的个数。元素顺序是任意的。如果一个元素的计数小于1， elements() 就会忽略它。
c = Counter(a=4, b=2, c=0, d=-2)
print list(c.elements()) # ['a', 'a', 'a', 'a', 'b', 'b']
# most_common
print Counter('abracadabra').most_common(1) # [('a', 5)]
# subtract([iterable-or-mapping]) 从 迭代对象 或 映射对象 减去元素。
# 像 dict.update() 但是是减去，而不是替换。输入和输出都可以是0或者负数。
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print c # Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})
# 其他操作同字典， 两个例外不支持：fromkeys update

# 4. OrderedDict 字典的子类，保存了他们被添加的顺序
# regular unsorted dictionary
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
# dictionary sorted by key
OrderedDict(sorted(d.items(), key=lambda t: t[0]))
# OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])
# dictionary sorted by value
OrderedDict(sorted(d.items(), key=lambda t: t[1]))
# OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])
# dictionary sorted by length of the key string
OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
# OrderedDict([('pear', 1), ('apple', 4), ('orange', 2), ('banana', 3)])

# 5. defaultdict 字典的子类，提供了一个工厂函数，为字典查询提供一个默认值
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
print d.items()
# same as:
d = {}
for k, v in s:
    d.setdefault(k, []).append(v) # D.get(k,d), also set D[k]=d if k not in D
print d.items()
# same as:
d = {}
for k, v in s:
    if not d.get(k):
        d[k] = []
    d[k].append(v)
print d.items()

