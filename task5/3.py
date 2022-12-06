n=str(input())
l=len(n)
while sum!=1 and sum!=37:
   sum = 0
   for i in range (l):
       sum=sum+(int(n[i])*int(n[i]))
   n=str(sum)
if sum==37:
   print("false")
if sum==1:
   print("true")
