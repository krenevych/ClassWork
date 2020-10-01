a, b, c = map(float, input().split())
# a, b, c = [float(i) for i in input().split()]

teor1 = a ** 2 + b ** 2 == c ** 2
teor2 = c ** 2 + a ** 2 == b ** 2
teor3 = c ** 2 + b ** 2 == a ** 2


if teor1 or teor2 or teor3:
    print("YES")
else:
    print("NO")
