a, b, c = map(float, input().split())

cond = (a ** 2 + b ** 2 == c ** 2 or
        b ** 2 + c ** 2 == a ** 2 or
        c ** 2 + a ** 2 == b ** 2)
if cond:
    print("YES")
else:
    print("NO")
