n=list(map(int,input().split()))
L=len(n)
def PlusOne(n):
    ind=L-1
    while(ind>=0) and(n[ind]==9) :
        n[ind]=0
        ind=ind-1
    if (ind<0):
        n.insert(0.1)
    else:
        n[ind]=n[ind]+1
PlusOne(n)
print(n)