N = int(input())
d = [i for i in range(N, -1, -1)]
for i in range(N // 2, 0, -1):
    d[i] = (min(d[i * 2], d[i+1]) if i > N // 3 else min(d[i * 2], d[i+1], d[i*3])) + 1

print(d[1])