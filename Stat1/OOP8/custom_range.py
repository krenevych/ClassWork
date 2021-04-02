
def range(n0, n_last, step=1):
    n = n0
    yield n
    while True:
        n = n + step
        if n >= n_last:
            break
        yield n


for i in range(2, 10):
    print(i)