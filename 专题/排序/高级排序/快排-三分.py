# 分为三部分：
# 1. < target: [i] 与 < 区右边第一个交换，< 区右扩，i ++
# 2. = target: i ++
# 3. > target: [i] 与 > 区左边第一个交换，> 区左扩，i 不变，因为这种换过来的数没有判断过。
def partition(li, target):
    n = len(li)
    i, l, r = 0, -1, n
    while i < r:
        if li[i] == target: i += 1
        elif li[i] < target:
            li[l+1], li[i] = li[i], li[l+1]
            i += 1
            l += 1
        else:
            li[r-1], li[i] = li[i], li[r-1]
            r -= 1

def test():
    import random
    li = [random.randint(0,7) for _ in range(30)]
    print(li)
    partition(li, 3)
    print(li)

if __name__ == '__main__':
    test()

