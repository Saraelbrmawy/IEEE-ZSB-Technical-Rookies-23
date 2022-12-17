x=int(input())

y=[int(i) for i in str(x)]

a=int(y[0])

b=int(y[1])

c=int(y[2])

d=int(y[3])

if (a==b) or (b==c) or (c==d) or (a==d) or (c==a) or (b==d):
    while (a==b) or (b==c) or (c==d) or (a==d) or (c==a) or (b==d):

         x=x+1
         y=[int(i) for i in str(x)]
         a=int(y[0])
         b=int(y[1])
         c=int(y[2])
         d=int(y[3])
elif (a!=b) or(b!=c) or (c!=d) or (a!=d) or (c!=a) or (b!=d):
    x=x+1
    y=[int(i) for i in str(x)]
    a=int(y[0])
    b=int(y[1])
    c=int(y[2])
    d=int(y[3])

while (a==b) or (b==c) or (c==d) or (a==d) or (c==a) or (b==d):

    x=x+1

    y=[int(i) for i in str(x)]

    a=int(y[0])

    b=int(y[1])

    c=int(y[2])

    d=int(y[3])
print(x)

