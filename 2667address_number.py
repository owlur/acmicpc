N = int(input())
m = [list(map(int, input())) for _ in range(N)]
d = [[0] * N for _ in range(N)]
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
ans = []

def dfs(x, y):
    if d[x][y] or not m[x][y]:
        return 0

    res = 1
    d[x][y] = 1

    points = map(lambda mov_p: (x+mov_p[0], y+mov_p[1]), move)
    res += sum([dfs(moved_x, moved_y) for moved_x, moved_y in points
                if 0 <= moved_x < N and 0 <= moved_y < N])
    return res

for i in range(N):
    for j in range(N):
        if not d[i][j] and m[i][j]:
            ans.append(dfs(i, j))

print(len(ans), *sorted(ans), sep='\n')