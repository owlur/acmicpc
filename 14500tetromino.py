import sys

read = sys.stdin.readline

N, M = map(int, read().split())
paper = [list(map(int, read().split())) for _ in range(N)]
move = [(1,0), (-1,0), (0, 1), (0, -1)]


def search(blocks, s):
    if len(blocks) == 4:
        return s

    res = s
    for block in blocks:
        for x, y in move:
            x += block[0]
            y += block[1]
            if not (i,j) in blocks and 0 <= x < N and 0 <= y < M:
                res = max(search(blocks + [(x, y)], s + paper[x][y]), res)
    return res

ans = 0
for i in range(N):
    for j in range(M):
        point = paper[i][j]
        ans = max(search([(i,j), (i+1, j)], point + paper[i+1][j]) if 0 <= i+1 < N else point,
                  search([(i,j), (i, j+1)], point + paper[i][j+1]) if 0 <= j+1 < M else point,
                  ans)
print(ans)