def prime(n):
    for i in range(2, (int)(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# print(prime(5))  # n = 5
# print(prime(15))
# print(prime(9))
# print(prime(121))

n = int(input("Уведіть n "))

print("range = [%d, %d]" % (n, 2 * n))

for i in range(n, 2 * n - 1):
    print(i)
    if prime(i) and prime(i + 2):
        print(i, i + 2)
