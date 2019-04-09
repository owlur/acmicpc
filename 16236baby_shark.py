N = int(input())
m = []
for r in range(N):
    row = list(map(int, input().split()))
    f = True if 9 in row else None
    if f:
        c = row.index(9)
        shark = [r,c]
        row[c] = 0
    m.append(row)
eaten_num = 0
size = 2
t = 0

while True:
    q = [(*shark, 0)]
    visited = [[0] * N for _ in range(N)]
    eatable_fishes = []
    while q:
        r, c, n = q.pop()
        if eatable_fishes and eatable_fishes[0][2] == n:
            break

        for i, j in ((r, c + 1), (r, c - 1), (r - 1, c), (r + 1, c)):
            if 0 <= i < N and 0 <= j < N and not visited[i][j]:
                if m[i][j] == 0 or m[i][j] == size:
                    q = [(i, j, n + 1)] + q
                elif m[i][j] < size:
                    eatable_fishes.append((i,j,n + 1))
                visited[i][j] = 1

    if not eatable_fishes:
        break
    min_r = min_c = N
    for i, j, n in eatable_fishes:
        if i < min_r or (i == min_r and j < min_c):
            min_r = i
            min_c = j
    t += n
    eaten_num += 1
    m[min_r][min_c] = 0
    shark = [min_r, min_c]
    if eaten_num == size:
        eaten_num = 0
        size += 1
print(t)