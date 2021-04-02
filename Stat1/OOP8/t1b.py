def generator(N):
    S = 1
    yield S

    for n in range(2, N + 1):
        S += 1 / n
        yield S


for i in generator(20):
    print(i)