

#  5! = 1 * 2 * 3 * 4 * 5

n = int(input())
fact = 1
i = 1

while i <= n:
    fact *= i
    # fact = fact * i
    print("%d! = %d" % (i, fact))
    i += 1  # i = i + 1

print(fact)
