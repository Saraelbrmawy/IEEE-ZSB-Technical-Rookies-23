array =list(map(int,input().split()))
List=[]
s=0
M=len(array)
for i in range(0,M):
    for j in range((i+1),M):
        if array[i]==array[j]:
          s=abs(j-i)
          array.append(s)
print(s)