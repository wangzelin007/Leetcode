var1=object; var2=var1
print(id(var1), id(var2))
# 139697863383968 139697863383968

a=123; b=a; print(id(a), id(b))
# 23242832 23242832
a=456; print(id(a), id(b))
# 33166408 23242832

a=1; b=1; print(a is b) # True
c="good"; d="good"; print(c is d) # True
e="very good"; f="very good"; print(e is f) # py2 False py3 True
g=[]; h=[]; print(g is h) # False

from sys import getrefcount
a=[1,2,3]; print(getrefcount(a)) # 2
b=a; print(getrefcount(a), getrefcount(b)) # 3 3

a=[1,2,3,4,5]; b=a; print(a is b) # True
a[0]=6; print(a) # [6, 2, 3, 4, 5]
print(a is b) # True
print(b) # [6, 2, 3, 4, 5]
print(getrefcount(123)) # 6
n=123; print(getrefcount(123)) # 7
m=n; print(getrefcount(123)) # 8
a=[1,12,123]; print(getrefcount(123)) # 9

del m; print(getrefcount(123)) # 8
n=456; print(getrefcount(123)) # 7
a.remove(123); print(a) # [1, 12]
print(getrefcount(123))# 6

import gc
print(gc.get_threshold()) # gc模块中查看阈值的方法
# (700, 10, 10)
print(gc.collect())    # 手动启动垃圾回收
# 0