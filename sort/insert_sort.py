def insert_sort(l):
    for i in range(1, len(l)):
        j = i - 1
        key = l[i]
        while l[j] > key and j >= 0:
            l[j + 1] = l[j]
            j -= 1
        l[j+1] = key


test_l = [[4,2,5,1,8,3,2,4], [1,2,3,4,5], [5,4,3,2,1], [1,3,2,3], [3,3,3,4]]
for l in test_l:
    insert_sort(l)
    print(l)