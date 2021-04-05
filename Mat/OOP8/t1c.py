def D():
    D_n2 = 5   # Змінна для
               # зберігання n-2 члена послід.
    yield D_n2
    D_n1 = 19  # Змінна для
               # зберігання n-1 члена послід.
    yield D_n1

    while True:
        D_n1, D_n2 = 5 * D_n1 - 6 * D_n2, D_n1
        yield D_n1

# genD = D()
# for i in range(10):
#     print(next(genD))

for d in D():
    if d > 10000000:
        break
    print(d)