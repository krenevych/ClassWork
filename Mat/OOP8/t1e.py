def generate_exp(x):
    a = 1
    S = 1
    n = 0
    yield S, a
    while True:
        n += 1
        a *= x / n
        S += a
        yield S, a


for e, a in generate_exp(1):
    print(e)
    if abs(a) < 0.0000001:
        break
