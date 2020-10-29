
s = input()

counter = 0
for c in s[1:]:
    if c == "+" or c == "-" or c == "*":
        counter += 1

print(counter)