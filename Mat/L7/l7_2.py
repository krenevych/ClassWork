def prime(n):
    for i in range(2, (int)(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def isSqr(n):
    sqr = int(n ** 0.5 + 0.5)
    sqr2 = sqr * sqr
    return sqr2 == n

def isPow5(n):
    if n == 1:
        return True

    pow5 = 1
    while pow5 < n:
        pow5 = pow5 * 5

    return pow5 == n

def isPow5_(n):
    div = n
    while div > 1:
        ost = div % 5
        if ost != 0:
            return False
        div = div // 5

    return True

lst = [int(i) for i in input().split()]
print(lst)

for el in lst:
    if prime(el):
        print("%d - просте" % el)
    if isSqr(el):
        print("%d - повний квадрат" % el)
    if isPow5(el):
        print("%d - степінь 5" % el)
