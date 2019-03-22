N = int(input())
d = [0,0,0]

for _ in range(N):
    cost = map(int, input().split())
    d = [min(c + d[i+1 if i < 2 else 0], c + d[i-1]) for i, c in enumerate(cost)]

print(min(d))