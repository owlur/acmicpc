s1, s2 = input(), input()
d = [[] for _ in range(len(s2))]

for i in range(len(s1)):
    p = []
    for j in range(len(s2)):
        if len(d[j]) > len(p): p = d[j]
        elif s1[i] == s2[j] and len(d[j]) <= len(p): d[j] = p + [i]

ans = []
for i in d:
    if len(i) > len(ans):
        ans = i
print(len(ans))
print(''.join(map(lambda x:s1[x], ans)))