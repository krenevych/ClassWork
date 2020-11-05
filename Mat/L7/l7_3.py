def max2(a, b):
    return a if a > b else b


def min2(a, b):
    return a if a < b else b

def min3(a, b, c):
    return min2(a, min2(b, c))

x, y, z = [float(i) for i in input().split()]
res = min3(max2(x, y), max2(y, z), x + y + z)
print("%0.2f" % res)
