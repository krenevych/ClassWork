
n = int(input("n = "))

sot = n // 100
od = n % 10
dec = (n // 10) % 10

# print(sot, dec, od)

Cond_a = sot == 2 or dec == 2 or od == 2
Cond_b = sot % 2 == 0 and dec % 2 == 0 and od % 2 == 0
Cond_c = sot + dec + od == 18

print(Cond_a)
print(Cond_b)
print(Cond_c)