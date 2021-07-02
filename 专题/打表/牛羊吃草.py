# 仓库有N份青草，一只牛一只羊
# 牛先吃草，羊后吃草，每一轮吃的草只能是4的某次方
# 1, 4, 16, 64
# 谁先吃完草谁获胜，根据N，返回获胜的一方。
from functools import lru_cache

@lru_cache(None)
def winner(n):
    if n < 5: return '后手' if n == 0 or n == 2 else '先手'
    base = 1
    while base <= n:
        if (winner(n-base)) == '后手':
            return '先手'
        # if base > n / 4: break # java 防止溢出
        base *= 4
    return '后手'

# 通过找规律发现了 处于后先后先先的循环
def winner2(n):
    if n % 5 == 0 or n % 5 == 2: return '后手'
    else: return '先手'

def test():
    for i in range(100):
        assert winner(i) == winner2(i)

if __name__ == '__main__':
    test()