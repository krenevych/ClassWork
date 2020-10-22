N = int(input())
lst = [float(i) for i in input().split()]

suma = 0
counter = 0
for i in range(2, N, 3):
    if lst[i] > 0:
        suma += lst[i]
        counter += 1

print(counter, "%0.2f" % suma)
