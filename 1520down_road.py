def route(n, x, y):
    if x == N -1 and y == M - 1:
        return 1
    if d[y][x] > -1:
        return d[y][x]
    X = []
    Y = []
    if x > 0: X.append(x-1)
    if x < N -1: X.append(x+1)
    if y > 0: Y.append(y-1)
    if y < M -1: Y.append(y+1)

    a = 0
    for p in X:
        if r[y][p] < n:
            a += route(r[y][p], p, y)
    for p in Y:
        if r[p][x] < n:
            a += route(r[p][x], x, p)
    d[y][x] = a
    return a

M, N = map(int,input().split())
r = [tuple(map(int, input().split())) for _ in range(M)]
d = [[-1]*N for _ in range(M)]
print(route(r[0][0],0,0))