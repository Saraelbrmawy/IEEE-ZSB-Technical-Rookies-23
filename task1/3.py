n = int(input())
x = input().split()
list1 = []
j = fsum = ssum = tsum =0
for i in range(0,n):
    list1.append(int(x[i]))

for i in range(0,n):
    fsum += list1[i]
print(fsum)

while (j < n) :
    ssum += list1[j]
    j+=1
print(ssum)
def third(list,size):
     if size==0:
         return 0
     else:
         return list[size - 1] + third(list,size - 1)
tsum = third(list1,n)
print(tsum)