N = int(input())
lst = [float(i) for i in input().split()]

suma = 0
count = 0
# [6, 7.5, 2.1, 2.0, 0, -3]
# [0,   1,   2,   3, 4,  5]

for i in range(2, N, 3):
    if lst[i] > 0:
        suma += lst[i]
        count += 1

print(count, "%0.2f" % suma)