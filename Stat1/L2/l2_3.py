n = int(input())

cond1 = n % 2 != 0
cond2 = 100 <= n <= 999

if cond1 or cond2:
    print("YES")
else:
    print("NO")