
n = int(input())

res1 = 0 # кiлькiсть двозначних чисел, цифри яких спадають
res2 = 0 # кiлькiсть двозначних чисел, цифри яких зростають
res3 = 0 # кiлькiсть двозначних чисел, цифри яких мають однакову парність.
res4 = 0 # суму двозначних чисел, цифри яких однакові.
res5 = 0 # суму двозначних чисел, цифри яких парні.
res6 = 0 # суму двозначних чисел, цифри яких непарні.

for i in range(10, 100):
    d = i // 10  # i = 32
    o = i % 10

    if d > o:
        res1 += 1

    if d < o:
        res2 += 1

    if o % 2 == d % 2:
        res3 += 1

    if o == d:
        res4 += i

    if o % 2 == 0 and d % 2 == 0:
        res5 += i

    if o % 2 != 0 and d % 2 != 0:
        res6 += i

if n == 1:
    print(res1)
elif n == 2:
    print(res2)
elif n == 3:
    print(res3)
elif n == 4:
    print(res4)
elif n == 5:
    print(res5)
else:
    print(res6)