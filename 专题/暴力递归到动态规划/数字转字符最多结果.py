# coding: utf-8
# 规定 1 与 A 对应，2 与 B 对应，3 与 C 对应
# 比如一个数字 111 可以对应为 AAA or AK or KA
# 给定一个只由数字组成的字符串，返回最多对应的数量
def mostStr(s):
    if not s or len(s) == 0:
        return 0
    s = list(s)

    def process(s, i):
        if len(s) == i:
            return 1
        if s[i] == '0':
            return 0
        if s[i] == '1':
            res = process(s, i+1) # 自己单独一定满足
            if i+1 < len(s):
                res += process(s, i+2)
            return res
        if s[i] == '2':
            res = process(s, i+1) # 自己单独一定满足
            if i+1 < len(s) and s[i+1] >= '0' and s[i+1] <= '6':
                res += process(s, i+2)
            return res
        # == '3'~'9'
        return process(s, i+1)

    return process(s, 0)

def mostStr2(s):
    n = len(s)
    if not s or n == 0:
        return s
    s = list(s)
    dp = [0 for _ in range(n+1)]
    dp[n] = 1
    for i in range(n-1, -1, -1):
        if s[i] == '0':
            dp[i] = 0
        elif s[i] == '1':
            dp[i] = dp[i+1]
            if i+1 < n:
                dp[i] += dp[i+2]
        elif s[i] == '2':
            dp[i] = dp[i+1]
            if i+1 < n and s[i+1] >= '0' and s[i+1] <= '6':
                dp[i] += dp[i+2]
        else: # 3-9
            dp[i] = dp[i+1]
    return dp[0]


def test():
    s = '11111'
    print(mostStr(s))
    assert mostStr(s) == mostStr2(s)

if __name__ == '__main__':
    test()