"-1+2*3+a"
"1+2*3+a"

s = input()

counter = 0
for c in s:
    if c in "AEIOUIY":
        counter += 1

print(counter)