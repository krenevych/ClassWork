
def prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


n = int(input("n = "))

print("[%d, %d]" % (n, 2*n))

for i in range(n, 2 * n - 1):
    if prime(i) and prime(i + 2):
        print(i, i + 2)
