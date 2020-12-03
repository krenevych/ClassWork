
a = input()

sum_cil = 0
sum_dro = 0
flag_is_cil = True

for c in a:
    if c == '.':
        flag_is_cil = False
        continue

    if not c.isdigit():
        continue

    d = int(c)
    if flag_is_cil:
        sum_cil += d
    else:
        sum_dro += d

if (sum_cil == sum_dro):
    print("Yes")
else:
    print("No")

