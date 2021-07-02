# 每一圈结束位置和下一圈开始位置接壤
def PrintMatrixOrder(matrix):
    a, b, c, d = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
    while a <= c and b <= d:
        printEdge(matrix, a, b, c, d)
        a += 1
        b += 1
        c -= 1
        d -= 1

def printEdge(m, a, b, c, d):
    # 横线
    if a == c:
        for i in range(b, d + 1):
            print(m[a][i], end=',')
    # 竖线
    elif b == d:
        for i in range(a, c + 1):
            print(m[i][b], end=',')
    else:
        curR, curC = a, b
        while curC != d:
            print(m[a][curC], end=',')
            curC += 1
        while curR != c:
            print(m[curR][d], end=',')
            curR += 1
        while curC != b:
            print(m[c][curC], end=',')
            curC -= 1
        while curR != a:
            print(m[curR][b], end=',')
            curR -= 1


def test():
    matrix = [['a','b','c','d','e'],
              ['p','q','r','s','f'],
              ['o','x','y','t','g'],
              ['n','w','v','u','h'],
              ['m','l','k','j','i']]
    PrintMatrixOrder(matrix)

if __name__ == '__main__':
    test()