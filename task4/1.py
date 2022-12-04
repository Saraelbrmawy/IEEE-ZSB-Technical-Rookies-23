import heapq
def mostFrequentNumber(arr, N, K):
    mp = dict()
    for i in range(0, N):
        if arr[i] not in mp:
            mp[arr[i]] = 0
        else:
            mp[arr[i]] += 1
    heap = [(value, key) for key, value in mp.items()]
    largest = heapq.nlargest(K, heap)

    for i in range(K):
        print(largest[i][1])

arr = [1,1,1,2,2,3]
N = len(arr)
K = 2
mostFrequentNumber(arr,N,K)