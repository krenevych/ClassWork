
# a   b
# 12 15
# 15 12
# 12 15 % 12 = 3
# 3  12 % 3 = 0
# 3  0

def nsd(a, b):
    if a < b:
        return nsd(b, a)
    if b == 0:
        return a
    else:
        return nsd(b, a % b)


# print(nsd(12, 15))
# print(nsd(2 * 3 * 5 * 7 * 13, 5 * 7 * 11 * 19))

a, b = [int(i) for i in input().split()]
print(nsd(a, b))