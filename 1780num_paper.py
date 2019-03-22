def divide(x,y,n):
    res = [0,0,0]
    num = p[x][y]

    for i in p[x: x+n]:
        if not all((1 if j == num else 0 for j in i[y: y + n])):
            break
    else:
        res[num] = 1
        return res

    n3 = n//3
    for i in range(x, x+n, n3):
        for j in range(y, y+n, n3):
            r1, r2, r3 = divide(i,j,n3)
            res[0] += r1
            res[1] += r2
            res[2] += r3
    return res

N = int(input())
p = [list(map(int,input().split())) for _ in range(N)]
ans = divide(0,0,N)
ans.insert(0, ans.pop())
print('%d\n%d\n%d'%(ans[0], ans[1], ans[2]))