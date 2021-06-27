# 返回等于区域的位置范围
def netherlandsFlags(li, L, R):
    if L > R: return [-1, -1]
    if L == R: return [L, R]
    less = L - 1
    more = R
    index = L
    while index < more:
        if li[index] == li[R]:
            index += 1
        elif li[index] < li[R]:
            li[index], li[less+1] = li[less+1], li[index]
            less += 1
            index += 1
        else:
            li[index], li[more-1] = li[more-1], li[index]
            more -= 1
    li[more], li[R] = li[R], li[more]
    print(li)
    return [less+1, more]

def test():
    li = [6, 0, 7, 2, 5, 6, 0, 7, 7, 3, 5, 5, 4, 7, 4, 5, 6, 1, 0, 0, 5, 7, 3, 7, 0, 7, 3, 1, 6, 3]
    print(li)
    print(netherlandsFlags(li, 0, 29))

if __name__ == '__main__':
    test()

