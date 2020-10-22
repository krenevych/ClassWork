n = int(input())
a = [int(el) for el in input().split()]

for i in range(n - 1):
    for j in range(n - 1 - i):
        if a[j] > a[j + 1]: # Якщо наступний елемент менший за попередній

            # Міняємо місцями елементи, тобто
            # виштовхуємо більший елемент нагору
            a[j], a[j + 1] = a[j + 1], a[j]
    print(*a)