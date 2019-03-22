s1, s2 = input(), input()

l1, l2 = len(s1), len(s2)

d = [[0] * (l2+1) for _ in range(l1+1)]

for i in range(l1-1, -1, -1):
    for j in range(l2-1, -1, -1):
        if s1[i] == s2[j]: d[i][j] = d[i+1][j+1] + 1
        else: d[i][j] = max(d[i][j+1], d[i+1][j])

for i in d:
    print(i)
print(d[0][0])
