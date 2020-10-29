
"welcome to python"

s = input()

res = ""

for c in s:
    res += c
    if c in "aeiouy":
        res += c

print(res)