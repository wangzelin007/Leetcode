# coding: utf-8
# 假设 A B 两人绝顶聪明
# 给定一个列表，表示 N 张牌
# 每轮每人只能从头或者尾拿一张牌
# 求最后赢家的点数和

def cardsInLine(arr):
    if not arr or len(arr) == 0:
        return 0
    l = 0
    r = len(arr) - 1
    return max(f(arr, l, r), s(arr, l, r))

def f(arr, l, r):
    if l == r:
        return arr[l]
    return max(arr[l] + s(arr, l+1, r), arr[r] + s(arr, l, r-1))

def s(arr, l, r):
    if l == r:
        return 0
    return min(f(arr, l+1, r), f(arr, l, r-1))

def winner(arr):
    n = len(arr)
    l, r = 0, n - 1
    if not arr or n == 0:
        return 0
    f = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]
    for j in range(n):
        f[j][j] = arr[j]
        for i in range(j-1, -1, -1):
            # f[i][j] = max(f[i][i] + s[i+1][j], f[j][j] + s[i][j-1])
            f[i][j] = max(arr[i] + s[i+1][j], arr[j] + s[i][j-1])
            s[i][j] = min(f[i+1][j], f[i][j-1])
    return max(f[l][r], s[l][r])

def test():
    arr = [4,5,9,7]
    assert cardsInLine(arr) == 13
    assert winner(arr) == 13

if __name__ == '__main__':
    test()