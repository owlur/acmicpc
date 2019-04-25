def quick_sort(l, left, right):
    if left >= right:
        return

    pivot = l[left]
    low = left
    high = right
    while low < high:
        while low < high and l[low] <= pivot:
            low += 1
        while low <= high and l[high] > pivot:
            high -= 1
        if low < high:
            l[low], l[high] = l[high], l[low]

    l[left], l[high] = l[high], l[left]

    quick_sort(l, left, high - 1)
    quick_sort(l, high + 1, right)

test_l = [[4,2,5,1,8,3,2,4], [1,2,3,4,5], [5,4,3,2,1], [1,3,2,3], [3,3,3,4]]
for l in test_l:
    quick_sort(l, 0, len(l)- 1)
    print(l)