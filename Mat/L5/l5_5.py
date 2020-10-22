a0 = [float(el) for el in input().split()]
b0 = [float(el) for el in input().split()]

a = [a0[2] - a0[0], a0[3] - a0[1]]
b = [b0[2] - b0[0], b0[3] - b0[1]]

# 1
l_a = a[0] ** 2 + a[1] ** 2
l_b = b[0] ** 2 + b[1] ** 2

l_a = l_a ** 0.5
l_b = l_b ** 0.5

print("%0.9f %0.9f" % (l_a, l_b))

# 2
s = [a[0] + b[0], a[1] + b[1]]
print("%0.9f %0.9f" % (s[0], s[1]))

# 3
dot = a[0] * b[0] + a[1] * b[1]
cross = a[0] * b[1] - a[1] * b[0]
print("%0.9f %0.9f" % (dot, cross))

# 4
s = cross
s /= 2.0
print("%0.9f" % abs(s))