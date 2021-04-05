def Prod():
    ak_3 = 1
    P = ak_3
    k = 0
    yield P

    ak_2 = 1
    k = 1
    P *= ak_2 / 3
    yield P

    ak_1 = 3
    k = 2
    P *= ak_1 / 9
    yield P

    z = 9
    t = 2
    while True:
        z *= 3
        t *= 2
        ak_1, ak_2, ak_3 = ak_3 + ak_2 / t, ak_1, ak_2
        P *= ak_1 / z
        yield P


n = 0
for p in Prod():
    print(p)
    n += 1
    if n == 10:
        break
