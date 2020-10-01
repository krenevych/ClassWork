n = int(input("n = "))

cond_a = n % 2 == 0
cond_b = n % 10 == 0

print(cond_a)
print(cond_b)

dec = n // 10
od = n % 10
cond_c = dec + od > 9

print(cond_c)
