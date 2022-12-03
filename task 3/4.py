
def NTurn(n, p):
    if(n%2==0):
        n=n+1
    return min ((p+1)/2,(n-p+1)/2)
n = int(input("enter the number of pages:"))
p = int(input("enter the number of page you want:"))
print(int(NTurn(n,p)))







