def merge_sort(l):
    if len(l) == 1 or not l:
        return l

    mid = len(l) // 2
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])

    new_l = []
    for i in range(len(l)):
        if not left:
            new_l.extend(right)
            break
        elif not right:
            new_l.extend(left)
            break
        else:
            new_l.append(left.pop(0) if left[0] < right[0] else right.pop(0))

    return new_l


test_l = [[4,2,5,1,8,3,2,4], [1,2,3,4,5], [5,4,3,2,1], [1,3,2,3], [3,3,3,4]]
for l in test_l:
    l = merge_sort(l)
    print(l)