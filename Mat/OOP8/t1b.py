def gen():
    S = 1
    n = 1
    yield S
    while True:
        n += 1
        S += 1 / n
        yield S


n = 5
k = 0
for el in gen():
    if k == n:
        break
    k += 1
    print(el)

