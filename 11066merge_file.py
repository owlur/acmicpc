def div(s, e):
    if e-s == 1:
        return 0
    if d[s][e] == -1:
        d[s][e] = min([div(s, i) + div(i, e) for i in range(s + 1, e)]) + sum(f[s:e])

    return d[s][e]

for _ in range(int(input())):
    K = int(input()) + 1
    f = list(map(int, input().split()))
    d = [[-1] * K for _ in range(K)]
    print(div(0, len(f)))