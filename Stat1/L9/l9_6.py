a = input()
b = input()

freq_a = {el: a.count(el) for el in a}
freq_b = {el: b.count(el) for el in b}
#
# print(freq_a)
# print(freq_b)

for k in freq_b:
    if k not in freq_a or freq_a[k] < freq_b[k]:
        print("No")
        break
else:
    print("Ok")