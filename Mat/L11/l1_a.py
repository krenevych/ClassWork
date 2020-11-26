

N = int(input("N= "))
x = float(input("x= "))

a = x
for k in range(2, N+1):
    a = x * (k-1) / k * a

print(a)