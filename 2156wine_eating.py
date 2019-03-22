w = [int(input()) for _ in range(int(input()))]
d = [(0,0,0), (0,w[0],0)]

for c in w[1:]:
    d.append((max(d[-1]), max(d[-2]) + c, d[-1][1] + c))

print(max(d[-1]))