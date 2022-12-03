n,m = map(int,input().split())
cities= sorted(map(int,input().split()))
m = max(n-cities[-1]-1,cities[0]-0)
for i in range(1,len(cities)):
    dis=int((cities[i]-cities[i-1])/2)
    if dis>m:
        m=dis
print(m)
