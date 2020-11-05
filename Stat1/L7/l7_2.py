def prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def isFulSquare(n):
    sqr = n ** 0.5
    sqr_int = int(sqr + 0.5)
    return sqr_int * sqr_int == n

# 1 5 25 125 625
def isPow5(n):  # n = 125
    if n == 1:
        return True

    pow5 = 1
    while pow5 < n:
        pow5 = pow5 * 5

    return pow5 == n

########################################
########################################

lst = [int(i) for i in input().split()]
print(lst)

l_prime = []
l_fulSqr = []
l_pow5 = []

for el in lst:
    if prime(el):
        l_prime.append(el)
    if isFulSquare(el):
        l_fulSqr.append(el)
    if isPow5(el):
        l_pow5.append(el)

print("Повні квадрати:", l_fulSqr)
print("Степені 5:", l_pow5)
print("Прості числа:", l_prime)
