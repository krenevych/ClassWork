a = input()
freq_a = {elem: a.count(elem) for elem in a}

b = input()
freq_b = {elem: b.count(elem) for elem in b}

# print(freq_a)
# print(freq_b)

posible = True
for key in freq_b:
    if key not in freq_a or freq_a[key] < freq_b[key]:
        posible = False
        break

if posible:
    print("Ok")
else:
    print("No")