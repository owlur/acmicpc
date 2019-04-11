def dfs(m, r, count):
    results = []
    for i in range(r, 10):
        if 1 in m[i]:
            j = m[i].index(1)
            break
    else:
        return count

    for k in range(5):
        if i+k < 10 and j+k < 10 and all(m[i+k][j:j+k+1]) and all((row[j+k] for row in m[i:i+k])):
            if count[k] > 4:
                continue
            new_m = [row.copy() for row in m]
            for new_i in range(i, i+k+1):
                new_m[new_i][j:j+k+1] = [0]*(k+1)
            new_count = count.copy()
            new_count[k] += 1
            result = dfs(new_m, i, new_count)

            if result != -1: results.append(result)
        else:
            break

    return min(results, key=lambda x: sum(x)) if results else -1

paper = []
for _ in range(10):
    paper.append(list(map(int, input().split())))

res = dfs(paper, 0, [0, 0, 0, 0, 0])
print(sum(res) if res != -1 else -1)
