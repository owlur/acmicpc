grid = [list(input()) for _ in range(12)]
combo = 0

def dfs(x, y):
    if visit[x][y]:
        return []
    visit[x][y] = 1
    results = [(x,y)]
    for i,j in ((0,1), (0,-1), (1,0), (-1,0)):
        if 0 <= x+i< 12 and 0<= y+j < 6 and grid[x][y] == grid[x+i][y+j]:
            results.extend(dfs(x + i, y + j))
    return results


while True:
    visit = [[0] * 6 for _ in range(12)]

    exist = 0
    for r in range(12):
        for c in range(6):
            if grid[r][c] != '.':
                result = dfs(r,c)
                if len(result) > 3:
                    exist = 1
                    for x,y in result:
                        grid[x][y] = '.'

    if not exist:
        break

    empty_slots = [0] * 6

    for r in range(11, -1, -1):
        for c in range(6):
            if grid[r][c] == '.' and empty_slots[c] < r:
                empty_slots[c] = r
            if grid[r][c] != '.' and r < empty_slots[c]:
                grid[empty_slots[c]][c], grid[r][c] = grid[r][c], '.'
                empty_slots[c] -= 1
    combo += 1

print(combo)