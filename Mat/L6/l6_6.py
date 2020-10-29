


s = input()

s1 = ""

for c in s:
    if  c.isalnum() or c == " ":
    # if ("a" <= c <= "z" or
    #         "A" <= c <= "Z" or
    #             "0" <= c <= "9" or
    #                 c == " "):
        s1 += c

lst = s1.split()
n = len(lst)
print(n)

