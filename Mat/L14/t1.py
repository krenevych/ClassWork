a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

try:
    assert a + b > c and a + c > b and b + c > a
    p = (a + b + c) / 2.0
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print("Площа трикутника = ", s)
except AssertionError:
    print("Трикутника з такими сторонами не існує!")



