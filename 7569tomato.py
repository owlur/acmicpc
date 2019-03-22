import sys

r = sys.stdin.readline

M, N, H = map(int, r().split())
tomato_box = []
d = [[[0] * M for _ in range(N)] for _ in range(H)]
tomato_num = 0
rip_tomato = []

for i in range(H):
    tomato_box.append([])
    for j in range(N):
        row = list(map(int, r().split()))
        tomato_num += row.count(1) + row.count(0)
        rip_list = [(i, j, k) for k in range(len(row)) if row[k] == 1]
        if rip_list: rip_tomato.extend(rip_list)
        tomato_box[-1].append(row)

rip_tomato_num = len(rip_tomato)
move = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
count = 0
while rip_tomato_num < tomato_num:
    if not rip_tomato:
        print(-1)
        break

    now = rip_tomato.copy()
    rip_tomato = []
    for i, j, k in now:
        moving_point = map(lambda x: (i + x[0], j + x[1], k + x[2]), move)
        for x, y, z in moving_point:
            if 0 <= x < H and 0 <= y < N and 0 <= z < M and not d[x][y][z] and not tomato_box[x][y][z]:
                d[x][y][z] = 1
                rip_tomato_num += 1
                rip_tomato.append((x, y, z))
    count += 1
else:
    print(count)