N = [int(input()) for _ in range(int(input()))]
d = [(0,0), (N[0],0)]
for n in N[1:]:
    d.append((n + max(d[-2]), n + d[-1][0]))

print(max(d[-1]))