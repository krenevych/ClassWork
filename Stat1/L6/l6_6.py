s = input()

#  Hello  , world  !


# "a" <= c <= "z"  or "A" <= c <= "Z" or "0" <= c <= "9"
# same as c.isalnum()

new_s = ""
for c in s:
    if c.isalnum() or c == " ":
        new_s = new_s + c

words = new_s.split()

print(len(words))
