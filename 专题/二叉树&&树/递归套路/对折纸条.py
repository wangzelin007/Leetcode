def printAllFolds(n):
    printProcess(1, n, True)

def printProcess(i, n, down):
    if i > n: return
    printProcess(i+1, n, True)
    print("凹" if down else "凸", end="")
    printProcess(i+1, n, False)

def test():
    n = 3
    printAllFolds(n)

if __name__ == '__main__':
    test()