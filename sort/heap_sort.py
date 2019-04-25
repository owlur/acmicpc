# max heap

def heapify(l, node):
    n = len(l) - 1
    for children in ((2*node), (2*node+1)):
        if children <= n and l[children] > l[node]:
            l[node], l[children] = l[children], l[node]
            if children <= n//2:
                heapify(l, children)

def heap_sort(l):
    l = [0] + l
    n = len(l) - 1
    start_node = n // 2

    for i in range(start_node, 0, -1):
        heapify(l, i)

    l = l[1:]

    return l

test_set = [[1,2,3,4,5,6], [2,5,1,5,3,2,6], [4,3,2,1], [16, 14, 10, 4, 7, 9, 3, 2, 8, 1]]
for l in test_set:
    l = heap_sort(l)
    print(l)