n=int(input("enter the number of bottle:"))
v=[]
c=[]
sv=0
sc=0
for i in range (n):
    voulme,capcity=list(map(int,input().split()))
    sv+=voulme
    v.append(voulme)
    c.append(capcity)
if sv<=c[1]+c[2]:
    print("yes")
if sv>c[0]+c[1]:
    print("no")
