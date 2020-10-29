s = input()

counter = 0
for c in s:
    if c in "AEIOUY":
        counter += 1

print(counter)
