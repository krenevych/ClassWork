
n = int(input())

cond1 = n % 2 == 0 and n > 0
cond2 = n % 2 != 0 and n < 0

if not cond1 and not cond2:
    print("YES")
else:
    print("NO")

