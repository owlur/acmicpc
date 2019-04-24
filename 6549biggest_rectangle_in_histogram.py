import sys
read = sys.stdin.readline
sys.setrecursionlimit(999999)


def make_tree(start, end, node):
    if start > end:
        return -1
    elif end == start:
        tree[node] = (start, end, start)
        return tree[node]
    l = make_tree(start, (start + end) // 2, node * 2)
    r = make_tree(((start + end) // 2) + 1, end, (node*2)+1)
    tree[node] = (start, end, min((l,r), key=lambda x:buildings[x[2]])[2])
    return tree[node]

def find(start, end, node):
    leaf = tree[node]
    if start > leaf[1] or end < leaf[0]:
        return -1
    if start == leaf[0] and end == leaf[1]:
        return leaf[2]

    l = find(start, min(((leaf[0] + leaf[1]) // 2, end)), node*2)
    r = find(max((((leaf[0] + leaf[1]) // 2) + 1, start)), end, node*2 + 1)
    if l == -1: return r
    if r == -1: return l
    return min((l,r), key = lambda x:buildings[x])

def divide(start, end):
    if start > end:
        return -1
    index = find(start, end, 1)
    height = buildings[index]
    return max((height * (end - start + 1), divide(start, index-1), divide(index+1, end)))


r = read()
while r.strip() != '0':
    n, *buildings = map(int, r.split())
    tree = [-1] * (262144)
    make_tree(0, n-1, 1)
    print(divide(0, n - 1))
    r = read()