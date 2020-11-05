
def max2(a, b):
    return a if a > b else b

def min2(a, b):
    return a if a < b else b

def min3(a, b, c):
    return min2(min2(a, b), c)


x ,y, z = [float(i) for i in input().split()]

print(min3(max2(x,y), max2(y,z), x + y + z))