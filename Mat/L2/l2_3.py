
n = int(input())

Cond_1 = n % 2 == 1
Cond_2 = 100 <= n <= 999
Cond = Cond_1 or Cond_2

if Cond:
    print("YES")
else:
    print("NO")
