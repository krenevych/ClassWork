"   welcome    to    python  "

s = input()

res = s[0]

for c in s[1:]:
    if c != " ":
        res += c
    elif res[-1] != " ":
        res += c

if res[0] == " ":
    res = res[1:]

if res[-1] == " ":
    res = res[:-1]


print(res)
