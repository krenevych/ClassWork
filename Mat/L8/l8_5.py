
# 1 1 2 3
# F(0) = F(1) = 1
# F(n) = F(n-1) + F(n-2)

# fib_list = [1, 1, 2, 3]


def F(k):
    fib_list = []
    for n in range(k + 1):
        if n == 0:
            fib_list.append(0)
        elif n == 1:
            fib_list.append(1)
        else:
            f_n = fib_list[n - 1] + fib_list[n - 2]
            fib_list.append(f_n)
    # print(fib_list)
    return fib_list[k]


def NSD(a, b):
    if a < b:
        return NSD(b, a)
    if b == 0:
        return a
    else:
        return NSD(b, a % b)

#########################################
while True:
    try:
        n, m = [int(i) for i in input().split()]
        f1 = F(n)
        f2 = F(m)
        nsd = NSD(f1, f2)
        print(nsd % 100000000)
    except:
        break

