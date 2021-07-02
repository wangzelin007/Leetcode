#   A ->
# B [1  2  3  4  5  6
#    7  8  9  10 11 12
#    13 14 15 16 17 18]
# 按照：1 2 7 13 8 3 4 9 14 15 10 5 6 11 16 17 12 18 打印
# 宏观思考！！！不要纠结坐标变化。
def printMatrixZigZag(matrix):
    Ar, Ac, Br, Bc = 0, 0, 0, 0
    Endr = len(matrix) - 1
    Endc = len(matrix[0]) - 1
    fromUp = False
    while Ar != Endr + 1:
        printLevel(matrix, Ar, Ac, Br, Bc, fromUp)
        Ar = Ar + 1 if Ac == Endc else Ar
        Ac = Ac if Ac == Endc else Ac + 1
        Bc = Bc + 1 if Br == Endr else Bc
        Br = Br if Br == Endr else Br + 1
        fromUp = False if fromUp else True

def printLevel(m, Ar, Ac, Br, Bc, f):
    if f:
        while Ar != Br + 1:
            print(m[Ar][Ac],end=',')
            Ar += 1
            Ac -= 1
    else:
        while Br != Ar - 1:
            print(m[Br][Bc],end=',')
            Br -= 1
            Bc += 1

def test():
    matrix = [[1, 2, 3, 4, 5, 6],
              [7, 8, 9, 10, 11, 12],
              [13, 14, 15, 16, 17, 18]]
    printMatrixZigZag(matrix)

if __name__ == '__main__':
    test()