def modifiedkaprekarnumbers(n):
    d = len(str(n))
    nsqr = str(n * n)
    right = int(nsqr[len(nsqr) - d:])
    left = nsqr[:len(nsqr) - d]
    if left == '':
        left = 0
    left = int(left)
    return left + right == n
p = int(input())
q = int(input())
s=[]
for i in range(p, q + 1):
    if modifiedkaprekarnumbers(i):
        s.append(i)
if len(s) == 0:
    print("invalid range")
else:
    print(' '.join(str(c) for c in s))
