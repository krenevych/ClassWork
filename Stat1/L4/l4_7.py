n = int(input())

# n = 3 100, 999
# n = 4 1000, 9999
# n = 5 10000, 99999

if n == 1:
    print(4)
else:
    # for n in range(2, 11):
    #     start = 10 ** (n-1)
    #     end = 10 ** n
    #
    #
    #     counter = 0
    #     for i in range(start, end, 2):
    #         counter += 1
    #
    #     print(counter)

    print(45 * 10 ** (n - 2))

