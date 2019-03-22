import sys

sys.setrecursionlimit(99999)
for _ in range(int(input())):
    input()
    C = list(map(lambda x: int(x) - 1, input().split()))
    d = [0 for _ in range(len(C))]

    def dfs(i, n):
        if d[i]:
            if n == 0: return 0
            else: return 1
        d[i] = 1

        return dfs(C[i], n+1)

    print(sum([dfs(i,0) for i in range(len(C))]))