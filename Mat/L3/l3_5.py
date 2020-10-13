n = int(input())
# n = 256
prod = 1
suma = 0

while n > 0:
    ost = n % 10
    prod = prod * ost
    suma = suma + ost
    n = n // 10

# print(prod , suma)
print("%0.3f" % (prod / suma))