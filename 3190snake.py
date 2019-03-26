N = int(input())
apples = [[0] * N for _ in range(N)]
for _ in range(int(input())):
    i, j = map(lambda x:int(x) - 1, input().split())
    apples[i][j] = 1
moves = [input().split() for _ in range(int(input()))]


d = [[0]* N for _ in range(N)]
d[0][0] = 1

def turn(turn_dir):
    if move[0]:
        move[1] = -1 * move[0] if turn_dir == 'D' else move[0]
        move[0] = 0
    else:
        move[0] = move[1] if turn_dir == 'D' else move[1] * -1
        move[1] = 0

snake, move = [[0, 0]], [0, 1]
t, i, j = 1, 0, 1
while -1 < i < N and -1 < j < N:
    if d[i][j]:
        break

    snake.insert(0, (i,j))
    d[i][j] = 1

    if apples[i][j]:
        apples[i][j] = 0
    else:
        t_x, t_y = snake.pop()
        d[t_x][t_y] = 0

    if moves and int(moves[0][0]) == t:
        turn(moves[0][1])
        moves.pop(0)
    t += 1

    i += move[0]
    j += move[1]
print(t)