n = int(input())
res1 = 0 # кiлькiсть двозначних чисел, цифри яких спадають.
res2 = 0 # кiлькiсть двозначних чисел, цифри яких зростають
res3 = 0 # кiлькiсть двозначних чисел,
         # цифри яких мають однакову парність.
res4 = 0 # суму двозначних чисел, цифри яких однакові
res5 = 0 # суму двозначних чисел, цифри яких парні
res6 = 0 # суму двозначних чисел, цифри яких непарні

for i in range(10, 100):
    d = i // 10
    o = i % 10

    if d > o:
        res1 += 1

    if d < o:
        res2 += 1

    if o % 2 == d % 2:
        res3 += 1

    if d == o:
        res4 += i

    if d % 2 == 0 and o % 2 == 0:
        res5 += i

    if d % 2 != 0 and o % 2 != 0:
        res6 += i

if n == 1:
    print(res1)
if n == 2:
    print(res2)
if n == 3:
    print(res3)
if n == 4:
    print(res4)
if n == 5:
    print(res5)
if n == 6:
    print(res6)