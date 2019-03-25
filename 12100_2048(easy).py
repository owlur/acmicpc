import copy

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
if N == 1:
    print(board[0][0])
else:
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    s = [[board, 0]]
    c = 0
    max_num = max(map(max, board))
    while s:
        pre_board, c = s.pop()
        for m in range(4):
            d = [[0] * N for _ in range(N)]
            current_board = copy.deepcopy(pre_board)

            if move[m][1]:
                x_ran = [N]
                y_ran = (N - 2, -1, -1) if move[m][1] > 0 else [1, N]
            else:
                x_ran = (N - 2, -1, -1) if move[m][0] > 0 else [1, N]
                y_ran = [N]

            for i in range(*x_ran):
                for j in range(*y_ran):
                    if current_board[i][j] == 0:
                        continue
                    x = i + move[m][0]
                    y = j + move[m][1]
                    t = 0
                    while -1 < y < N and -1 < x < N:
                        if current_board[x][y]:
                            if current_board[x][y] == current_board[i][j] and not d[x][y]:
                                current_board[x][y] *= 2
                                if current_board[x][y] > max_num:
                                    max_num = current_board[x][y]

                                d[x][y] = 1
                                current_board[i][j] = 0
                            elif t:
                                current_board[x - move[m][0]][y - move[m][1]] = current_board[i][j]
                                current_board[i][j] = 0
                            break
                        x += move[m][0]
                        y += move[m][1]
                        t += 1
                    else:
                        current_board[x - move[m][0]][y - move[m][1]] = current_board[i][j]
                        current_board[i][j] = 0
            if c < 4:
                s.append((current_board, c + 1))
    print(max_num)