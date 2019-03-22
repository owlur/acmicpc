old = [0,0]
for _ in range(int(input())):
    new = list(map(int, input().split()))
    old = [0] + [new[i] + max(old[i], old[i+1]) for i in range(len(new))] + [0]

print(max(old))