n=int(input("enter the number of row and colum:"))
matrix=[]
for i in range(0,n):
    S=list(map(int,input().split()))
    matrix.append(S)
r=0
m=0
for i in range(n):
    for j in range(n):
        if i==j :
            r=r+matrix[i][j]
        if(i+j)==(n-1):
            m=m+matrix[i][j]
d=r-m
print(abs(d))


