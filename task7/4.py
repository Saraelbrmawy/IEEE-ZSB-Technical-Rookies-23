n=int(input())
class1=[]
grade=[]
for i in range(n):
    name=input()
    mark=float(input())
    class1.append([name,mark])
    grade.append(mark)
grade=sorted(set(grade))
m=grade[1]
name=[]
for val in class1:
    if m==val[1]:
        name.append(val[0])
name.sort()
for j in name:
    print(j)