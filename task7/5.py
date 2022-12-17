r = list(reversed([int(x) for x in input().split()]))
d= list(reversed([int(x) for x in input().split()]))

def calc(r, d):
    if r[0] < d[0]:
        return 0
    if r[0] > d[0]:
        return 10000
    if r[1] < d[1]:
        return 0
    if r[1] > d[1]:
        return 500 * (r[1] - d[1])
    if r[2] < d[2]:
        return 0
    if r[2] > d[2]:
        return 15 * (r[2] - d[2])
    return 0
print(calc(r, d))
