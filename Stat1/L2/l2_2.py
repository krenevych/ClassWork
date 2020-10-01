n = int(input("n = "))


od = n % 10
sot = n // 100
dec = n // 10 % 10

# print(sot, dec, od)

cond_a = sot == 2 or dec == 2 or od == 2
cond_b = (sot % 2 == 0) and (dec % 2 == 0) and (od % 2 == 0)
cond_c = sot + dec + od == 18
print(cond_a)
print(cond_b)
print(cond_c)