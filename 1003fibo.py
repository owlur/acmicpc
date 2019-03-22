d = [(1,0),(0,1)]

N = [int(input()) for _ in range(int(input()))]

for i in range(max(N) - 1):
    d.append((d[-1][0] + d[-2][0], d[-1][1] + d[-2][1]))

for i in N:
    print(d[i][0], d[i][1])