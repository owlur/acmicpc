p = [1,1,1,2,2,3,4,5]
for _ in range(int(input())):
    N = int(input())
    for i in range(len(p), N):
        p.append(p[-1] + p[-5])
    print(p[N-1])