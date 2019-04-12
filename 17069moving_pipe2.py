N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

d = [[[-1] * 3 for _ in range(N)] for _ in range(N)]
d[N-1][N-1] = [1,1,1]


def dfs(x,y,state):
    if d[x][y][state] != -1:
        return d[x][y][state]

    result = 0
    if state == 0:
        if y + 1 < N and not grid[x][y+1]:
            result += dfs(x,y+1,0)
            if x + 1 < N and not any((grid[x+1][y+1], grid[x+1][y])):
                result += dfs(x+1, y+1, 2)
    if state == 1:
        if x + 1 < N and not grid[x+1][y]:
            result += dfs(x+1,y,1)
            if y + 1 < N and not any((grid[x][y+1], grid[x+1][y+1])):
                result += dfs(x+1, y+1, 2)
    if state == 2:
        if y + 1 < N and not grid[x][y+1]:
            result += dfs(x,y+1,0)
        if x + 1 < N and not grid[x+1][y]:
            result += dfs(x+1,y,1)
        if x + 1< N and y + 1 < N and not any((grid[x][y+1], grid[x+1][y], grid[x+1][y+1])):
            result += dfs(x+1, y+1, 2)
    d[x][y][state] = result
    return result

print(dfs(0,1,0))