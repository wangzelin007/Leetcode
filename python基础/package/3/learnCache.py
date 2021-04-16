# http://kuanghy.github.io/2016/04/20/python-cache
# @functools.lru_cache(maxsize=None, typed=False)
from functools import lru_cache

@lru_cache(None)
def add(x, y):
    print("calculating: %s + %s" % (x, y))
    return x + y

print(add(1, 2))
print(add(1, 2))
print(add(2, 3))