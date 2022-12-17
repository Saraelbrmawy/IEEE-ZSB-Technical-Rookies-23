m =str(input())
s=[]
i=0
while i < len(m):
    if m[i]=='.' :
       s.append('0')
    elif m[i]=='-'and m[i+1] == '.':
        s.append('1' )
        i = i+1
    elif m[i] == '-' and m[i+1] == '-':
        s.append('2' )
        i = i+1
    i = i+1
print (''.join(s))
