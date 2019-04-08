import sys
read = sys.stdin.readline

N, M, K = map(int, read().split())
A = [tuple(map(int, read().split())) for _ in range(N)]
temp_trees = sorted([list(map(int, read().split())) for _ in range(M)],
               key=lambda x: x[2])

m = [[5] * N for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]
for r,c,a in temp_trees:
    trees[r-1][c-1].append(a)

for _ in range(K):
    breed = []

    for r in range(N):
        for c in range(N):
            for i, a in enumerate(trees[r][c]):
                if m[r][c] < a:
                    m[r][c] += sum(map(lambda x: x//2, trees[r][c][i:]))
                    trees[r][c] = trees[r][c][:i]
                    break
                if a % 5 == 4:
                    breed.append((r, c))
                m[r][c] -= a
                trees[r][c][i] += 1
            m[r][c] += A[r][c]

    for r,c in breed:
        for i, j in ((1,0), (1,1), (1,-1), (0,1), (0,-1), (-1,1), (-1,0), (-1,-1)):
            if 0 <= r + i < N and 0 <= c + j < N:
                trees[r+i][c+j] = [1] + trees[r+i][c+j]

print(sum(map(len, sum(trees, []))))