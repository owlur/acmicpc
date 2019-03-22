import sys

sys.setrecursionlimit(9999)

def rec(index):
    if t[index] == -1:
        t[index] = D[index] + (max(map(rec, d[index])) if d[index] else 0)

    return t[index]

for _ in range(int(input())):
    N, K = map(int,input().split())
    D = tuple(map(int, input().split()))
    d = {i:set() for i in range(N)}

    for i in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        d[Y-1].add(X-1)

    W = int(input()) - 1
    t = [-1 for i in range(N)]
    rec(W)
    print(t[W])
