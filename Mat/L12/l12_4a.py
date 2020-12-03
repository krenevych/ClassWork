eps = 0.00001
x = 13

a = x / 2
a_prev = a
n = 0

while True:
    n += 1
    a = 0.5 * (a + x / a)
    if abs(a - a_prev) < eps:
        break
    a_prev = a

print(a, n)
print(x ** 0.5)

# 13.000000062267958 6
# 13.0 7

# 13
# 3.6055512902583184 4
# 3.6055512754639896 5
# 3.605551275463989