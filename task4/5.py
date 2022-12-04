def rotate90Clockwise(A):
    N = len(A[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp


def printMatrix(A):
    N = len(A[0])
    for i in range(N):
        print(A[i])

n = int(input())
A=[]
for i in range(0,n):
    L= list(map(int,input().split()))
    A.append(L)
rotate90Clockwise(A)
printMatrix(A)

