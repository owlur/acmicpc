N = int(input())

d = [[1], [1]*9]

for i in range(N - 1):
    d.append([d[-2][0] + d[-1][1]] + [d[-1][i-1] + d[-1][i+1] for i in range(1,8)] + [d[-1][7]])

print(sum(d[-1]) % 1000000000)