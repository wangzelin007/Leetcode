# 以中心点旋转90度
# 还是分圈
def rotate(matrix):
    a, b, c, d = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
    while a < c:
        rotateEdge(matrix, a, b, c, d)
        a += 1
        b += 1
        c -= 1
        d -= 1

def rotateEdge(m, a, b, c, d):
    for i in range(d-b):
        tmp = m[a][b+i]       # 1 = tmp
        m[a][b+i] = m[c-i][b] # 1 = 4
        m[c-i][b] = m[c][d-i] # 4 = 3
        m[c][d-i] = m[a+i][d] # 3 = 2
        m[a+i][d] = tmp       # 2 = 1

def test():
    matrix1 = [[ 1, 2, 3, 4],
              [ 5, 6, 7, 8],
              [ 9,10,11,12],
              [13,14,15,16]]
    matrix2 = [[1,2,3],
              [4,5,6],
              [7,8,9]]
    rotate(matrix1)
    print(matrix1)
    rotate(matrix2)
    print(matrix2)

if __name__ == '__main__':
    test()