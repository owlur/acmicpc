N, M, x, y, K = map(int,input().split())
m = [list(map(int,input().split())) for _ in range(N)]
commands = list(map(int, input().split()))
dice = [0] * 6
move = [(0, 1), (0, -1), (-1, 0), (1, 0)]

# [윗면, 북쪽면, 아랫면, 남쪽면, 서쪽면, 동쪽면]
def rolling(c):
    if c == 1:
        dice[0], dice[2], dice[4], dice[5] = dice[4], dice[5], dice[2], dice[0]
    if c == 2:
        dice[0], dice[2], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[2]
    if c == 3:
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]
    if c == 4:
        dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]

for command in commands:
    temp_x = x + move[command-1][0]
    temp_y = y + move[command-1][1]
    if not(0 <= temp_x < N and 0 <= temp_y < M):
        continue
    x, y = temp_x, temp_y

    rolling(command)
    if m[x][y] == 0:
        m[x][y] = dice[2]
    else:
        dice[2] = m[x][y]
        m[x][y] = 0
    print(dice[0])

