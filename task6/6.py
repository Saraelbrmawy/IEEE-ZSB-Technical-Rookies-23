n, k, q = map(int, input().split())
arr = [int(x) for x in input().split()]
for _ in range(q):
    print(arr[int(input()) - k % n])