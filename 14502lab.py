import copy

N, M = map(int, input().split())
viruses = []
empty = []
lab = []
for i in range(N):
    lab.append([])
    for j, v in enumerate(map(int, input().split())):
        lab[-1].append(v)
        if v == 0:
            empty.append((i,j))
        if v == 2:
            viruses.append((i,j))

def bfs(x,y):
    res = 1 if new_lab[x][y] == 0 else 0
    new_lab[x][y] = 2

    for i, j in ((0,1), (0,-1), (1,0), (-1,0)):
        i += x
        j += y
        if 0<=i<N and 0<=j<M and new_lab[i][j] == 0:
            res += bfs(i,j)
    return res

c = len(empty)
ans = 0
for i in range(c):
    for j in range(i + 1, c):
        for k in range(j+1, c):
            new_lab = copy.deepcopy(lab)
            safe = c - 3
            for em in [i,j,k]:
                new_lab[empty[em][0]][empty[em][1]] = 1
                # print(empty[em][0], empty[em][1])

            for virus in viruses:
                safe -= bfs(virus[0], virus[1])
            ans = max(ans, safe)

print(ans)