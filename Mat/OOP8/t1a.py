def gen(x, N):
    a = 1
    yield a
    for n in range(1, N + 1):
        a *= x / n
        yield a

    # return a -> yield a


# print(req(10, 10))
# a_10(10) = 2755.7319223985896

def req1(x, N):
    a = 1
    for n in range(1, N + 1):
        a *= x / n

    return a

a_10 = req1(10, 10)
print(a_10)

g = gen(10, 10)
print(next(g))
print(next(g))
print(next(g))
print(next(g))


# for el in req(11, 11):
#     print(el)