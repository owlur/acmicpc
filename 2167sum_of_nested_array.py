N, M = map(int, input().split())
pre = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N + 1):
    for j, n in enumerate(map(int,input().split())):
        pre[i][j+1] = n + pre[i][j] + pre[i-1][j+1] - pre[i-1][j]

for _ in range(int(input())):
    i,j,x,y = map(int, input().split())
    print(pre[x][y] + pre[i-1][j-1] - pre[x][j-1] - pre[i-1][y])