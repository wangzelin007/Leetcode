from functools import lru_cache

@lru_cache
def fibo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

def fibo2(n):
    a = 0
    b = 1
    if n <= 0:
        return a
    elif n == 1:
        return b
    for i in range(2, n+1):
        a, b = b, a + b
    return b

def test():
    print(fibo(100))
    print(fibo2(100))

if __name__ == '__main__':
    test()