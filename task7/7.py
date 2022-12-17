def chocolateFeast(N, C,M):
    TOT = int(N/ C)
    if TOT >= M:
        W= int(TOT)
        while W > 0:
            W = W- M
            if W >= 0:
                TOT += 1
                W+= 1
    return TOT

t = int(input().strip())
for i in range(t):
    n, c, m = list(map(int, input().strip().split(' ')))
    print(chocolateFeast(n, c, m))