import sys
sys.setrecursionlimit(999999)

def dfs(i, cycle, height):
    if checked[i]:
        return height

    checked[i] = True
    cycle[i] = height
    res = cycle.get(numbers[i])

    if res is not None:
        return res
    else:
        return dfs(numbers[i], cycle, height + 1)

for _ in range(int(input())):
    n = int(input())
    numbers = list(map(lambda x: int(x) - 1, input().split()))
    checked = [False] * n
    print(sum((dfs(i, {}, 0) for i in range(n))))