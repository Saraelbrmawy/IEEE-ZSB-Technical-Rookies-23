def descorder(s):
    str1 = ''.join(sorted(s, reverse=True))
    return str(str1)
def is_Valid(number, n):
    freq = {}
    freq = set()
    for i in range(0, n):
        freq.add(number[i])
    if (len(freq) >= 2):
        return True
    return False
def Numberoftimes(number, n, cnt):
    if ((is_Valid(number, n) == False or n > 4) and cnt == 0):
        return -1
    elif (int(number) == 6174):
        return cnt
    cnt = cnt + 1

    while (n + 1 < 4):
        number[0] = '0'
    number2 = number
    res = ''.join(sorted(number))
    number = res
    number2 = descorder(number2)
    increasing = int(number)
    decreasing = int(number2)
    resstr = str(abs(increasing - decreasing))

    return Numberoftimes(resstr, len(resstr), cnt)

cnt = 0
number = str(input("enter the number:"))
n = len(number)

print(Numberoftimes(number, n, cnt))

