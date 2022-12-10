def beautiful_triplets(d, arr):
    arr_set = set(arr)
    count = 0
    for a in arr:
        if a+d in arr_set and a+2*d in arr_set:
            count += 1
    return count


n, d = map(int, input().split())
arr = list(map(int, input().rstrip().split()))
result = beautiful_triplets(d, arr)
print(result)