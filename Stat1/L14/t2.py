s = "asdfwe345klj2345jsd04452f34"
# s = "23474"
suma = 0
for c in s:
    try:
        suma += int(c)
    except ValueError:
        pass

print(suma)
