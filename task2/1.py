import random
s=random.randint(100,999)
k=str(s)
print(s)
while True:
 m=input("guess the number :")
 p=str(m)
 hit=0
 miss=0
 for i in range (3):
  if p[i] in k and k[i] == p[i]:
         hit=hit+1
  if p[i] in k and k[i]!=p[i]:
          miss=miss+1
 print(miss,"miss",hit,"hit")
 if hit==3:
     print("your gusses is correct")
     break;