def gedP(N):
    a_k3 = 1
    yield a_k3 # P_0

    a_k2 = 1
    yield a_k3 * a_k2 / 3

    a_k1 = 3
    z = 9
    P = 1 / 9
    yield P

    t = 2
    for k in range(3, N + 1):
        z *= 3
        t *= 2
        a_k1, a_k2, a_k3 = a_k3 + a_k2 / t, a_k1, a_k2
        P *= a_k1 / z
        yield P

for p in gedP(10):
    print(p)