import sys
N, M = int(sys.stdin.readline().strip()),int(sys.stdin.readline().strip())
ans = []
for x in range(max(3, N), M - 1):
    for y in range(x+1, M):
        for z in range(max(x+1,y+1,y-x+1), min(x + y,M + 1)):
            if x**2 + y**2 == z**2:
                ans.append((x,y,z))
ans = filter(lambda x: not(x[0] % 3 == x[1] % 4 == x[2] % 5), ans)
ans.insert(0, (3,4,5))
for a in ans:
    print(a[0], a[1], a[2])

# 如何判断是否互为质数
