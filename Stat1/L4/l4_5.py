n = int(input())

#  2 * 3 * 5 = 30

# 7 , 49, 343 [1, n^0.5]

if n % 2 == 0:
    print(2)
else:
    flag = True
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            print(i)
            flag = False
            break

    if flag:
        print(n)