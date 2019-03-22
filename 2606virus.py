n = int(input())

d = [[0] * n for _ in range(n)]
for _ in range(int(input())):
    x, y = map(lambda x: int(x) - 1, input().split())
    d[y][x] = d[x][y] = 1
a = [0 for _ in range(n)]
q = [0]
while q:
    i = q.pop()
    for j, p in enumerate(d[i]):
        if p and not a[j]:
            q.append(j)
    a[i] = 1

print(sum(a) - 1)
