s = input()

# welcome to python

new_s = ""

for c in s:
    new_s += c  # new_s = new_s + c
    if c in "aeiouy":
        new_s += c # new_s = new_s + c


print(new_s)
