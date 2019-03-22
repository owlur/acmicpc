n, k = map(int,input().split())

v = [int(input()) for _ in range(n)]
d=[1]+[0]*k
for i in v:
    for j in range(1,k+1):
        d[j] += d[j-i] if j >=i else 0

print(d[-1])