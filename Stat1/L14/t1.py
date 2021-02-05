def sqrTriangle(a, b, c):
    assert a + b > c and a + c > b and c + b > a

    p = (a + b + c) / 2.0
    s = p * (p - a) * (p - b) * (p - c)
    return s ** 0.5

while True:
    try:
        a, b, c = [float(el) for el in input("Введіть сторони трикутника").split()]
        s = sqrTriangle(a, b, c)
        print("Площа трикутника зі сторонами %f, %f, %f = %f" % (a, b, c, s))
        break
    except AssertionError:
        print("Трикутника з такими сторонами не існує")
