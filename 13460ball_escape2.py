N, M = map(int, input().split())
point = {'R': 0, 'B': 0, 'O': 0}
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
board = []
# move 의 좌표를 이용하여 보드 선택
moving_board = [[0, [[0] * M for _ in range(N)],
                 [[0] * M for _ in range(N)]],
                [[[0] * M for _ in range(N)], 0],
                [[[0] * M for _ in range(N)], 0]
                ]

for i in range(N):
    row = input()
    board.append(row)

    for c in point.keys():
        if row.find(c) > 0:
            point[c] = [i, row.find(c)]

for x, y in move:
    current_board = moving_board[x][y]
    x_ran = (N - 1, -1, -1) if x and x == 1 else [N]
    y_ran = (M - 1, -1, -1) if y and y == 1 else [M]


    for i in range(*x_ran):
        for j in range(*y_ran):
            if board[i][j] == '#':
                current_board[i][j] = -1
            elif board[i][j] in ['.', 'R', 'B']:
                pre_position = current_board[i + x][j + y]
                if pre_position == -1:
                    current_board[i][j] = [i, j]
                elif pre_position == 0:
                    current_board[i][j] = [i + x, j + y]
                else:
                    current_board[i][j] = pre_position
            elif board[i][j] == 'O':
                current_board[i][j] = 'E'

d = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

q = [(point['R'], point['B'], 0)]
while q:
    R_point, B_point, c = q.pop(0)
    if c >= 10:
        print(-1)
        break
    for x, y in move:
        moved_R = moving_board[x][y][R_point[0]][R_point[1]]
        moved_B = moving_board[x][y][B_point[0]][B_point[1]]
        moved_R = moved_R.copy() if moved_R != 'E' else moved_R
        moved_B = moved_B.copy() if moved_B != 'E' else moved_B

        if moved_B == moved_R and moved_B != 'E':
            if x:
                if x * (R_point[0] - B_point[0]) < 0:
                    moved_R[0] = moved_R[0] - x
                else:
                    moved_B[0] = moved_B[0] - x
            if y:
                if y * (R_point[1] - B_point[1]) < 0:
                    moved_R[1] = moved_R[1] - y
                else:
                    moved_B[1] = moved_B[1] - y

        elif moved_B == 'E':
            continue
        elif moved_R == 'E':
            print(c + 1)
            break

        if not d[moved_R[0]][moved_R[1]][moved_B[0]][moved_B[1]]:
            q.append((moved_R, moved_B, c + 1))
            d[moved_R[0]][moved_R[1]][moved_B[0]][moved_B[1]] = True
    else:
        continue
    break
else:
    print(-1)