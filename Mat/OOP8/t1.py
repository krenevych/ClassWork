def generate(x, N):
    a = 1
    yield a
    for n in range(1, N + 1):
        a *= x / n
        yield a
    # return a -> yield a


def generate_inf(x):
    a = 1
    n = 0
    yield a
    while True:
        n += 1
        a *= x / n
        yield a


for cur_a in generate_inf(1):
    print(cur_a)
    if abs(cur_a) < 0.001:
        break
