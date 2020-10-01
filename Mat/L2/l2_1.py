
n = 84

Cond_a = n % 2 == 0
Cond_b = n % 10 == 0

print(Cond_a)
print(Cond_b)

od = n % 10
dec = n // 10

Cond_c = od + dec >= 10
print(Cond_c)