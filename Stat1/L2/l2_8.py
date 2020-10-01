a, b, c = map(int, input().split())

# print(a, b, x, y, z )

if a < b < c:
    print(b)
elif c < b < a:
    print(b)
elif a < c < b:
    print(c)
elif b < c < a:
    print(c)
elif b < a < c:
    print(a)
else:
    print(a)

