
def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)
a = 12
b = 8
if (gcd(a, b)):
    print('GCD is:', gcd(a, b))
