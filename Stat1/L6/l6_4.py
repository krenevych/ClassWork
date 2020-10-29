s = input()

# "   Alexandr    Sergeevich   Pushkin   "
#          => "Alexandr Sergeevich Pushkin"

new_s = s[0]

for c in s[1:]:
    if c != " ":
        new_s += c
    else:
        if new_s[-1] != " ":
            new_s += c

if new_s[0] == " ":
    new_s = new_s[1:]

if new_s[-1] == " ":
    new_s = new_s[:-1]

print(new_s)

