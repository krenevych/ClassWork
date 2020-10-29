s = input()

# "WWWellcccooomee  ttoo PPyythooonn!!!"
#          => "Welcome to Python!"

new_s = s[0]

for c in s[1:]:
    if c != new_s[-1]:
        new_s += c

print(new_s)
