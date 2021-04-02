def genD():
    D_n2 = 5  # D_(n-2): зараз D_1
    yield D_n2
    D_n1 = 19  # D_(n-1): зараз D_2
    yield D_n1
    while True:
        D_n2, D_n1 = D_n1, 5 * D_n1 - 6 * D_n2
        yield D_n1


n = 1
for d in genD():
    print(d, n)
    if d > 10000000:
        break
    n += 1
