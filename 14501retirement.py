N = int(input())
TP = [tuple(map(int, input().split())) for _ in range(N)]
d = [0 for _ in range(N)]
for i in range(N-1, -1, -1):
    if i == N-1:
        if TP[i][0] <= 1:
            d[i] = TP[i][1]
    elif TP[i][0] + i > N:
        d[i] = d[i + 1]
    elif TP[i][0] + i == N:
        d[i] = max(TP[i][1], d[i + 1])
    else:
        d[i] = max(TP[i][1] + d[i + TP[i][0]], d[i+1])

print(d[0])