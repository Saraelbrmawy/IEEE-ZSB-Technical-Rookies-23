n=int(input())
for t in range(n):
    ivalue=int(input())
    cvalue=[float(i) for i in str(ivalue)]
    sum=0
    for c in cvalue:
        if c ==0:
            continue
        if(ivalue/c)%1==0:
            sum+=1
    print(sum)
