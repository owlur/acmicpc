def turn_90(m):
    return list(zip(*m[::-1]))

def turn__90(m):
    return list(zip(*(r[::-1] for r in m)))

def turn_p():
    global U
    F[0], L[0], B[0], R[0] = R[0], F[0], L[0][::-1], B[0][::-1]
    U = turn_90(U)

def turn_m():
    global U
    R[0], F[0], L[0], B[0] = F[0], L[0], B[0][::-1], R[0][::-1]
    U = turn__90(U)

def look(direction):
    global U, D, F, B, L, R
    if direction == 'L':
        U, D, F, B, L, R = turn_90(L), turn_90(R), turn_90(F), turn_90(B), turn_90(D), turn_90(U)
    elif direction == 'R':
        U, D, F, B, L, R = turn__90(R), turn__90(L), turn__90(F), turn__90(B), turn__90(U), turn__90(D)
    elif direction == 'F':
        U, D, F, B, L, R = F, B[::-1], D, U[::-1], turn__90(L), turn_90(R)
    elif direction == 'B':
        F, B, D, U, L, R = U, D[::-1], F, B[::-1], turn_90(L), turn__90(R)
    elif direction == 'D':
        U, D, F, B, L, R = D, U, B[::-1], F[::-1], turn_90(turn_90(L)), turn_90(turn_90(R))

ret = {'L': 'R', 'R': 'L', 'F': 'B', 'B': 'F', 'D': 'D', 'U': 'U'}

for _ in range(int(input())):
    U = [['w']*3 for _ in range(3)]
    D = [['y']*3 for _ in range(3)]
    F = [['r']*3 for _ in range(3)]
    B = [['o']*3 for _ in range(3)]
    L = [['g']*3 for _ in range(3)]
    R = [['b']*3 for _ in range(3)]
    # U = [['U1','U2','U3'], ['U4','U5','U6'], ['U7','U8','U9']]
    # D = [['D1','D2','D3'], ['D4','D5','D6'], ['D7','D8','D9']]
    # F = [['F1','F2','F3'], ['F4','F5','F6'], ['F7','F8','F9']]
    # B = [['B1','B2','B3'], ['B4','B5','B6'], ['B7','B8','B9']]
    # L = [['L1','L2','L3'], ['L4','L5','L6'], ['L7','L8','L9']]
    # R = [['R1','R2','R3'], ['R4','R5','R6'], ['R7','R8','R9']]

    n = int(input())
    cmd = input().split()
    for l, d in cmd:
        look(l)
        if d == '+': turn_p()
        else: turn_m()
        look(ret[l])

    for r in U:
        print(''.join(r))
    # print(U)