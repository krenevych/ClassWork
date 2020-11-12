
# "abc" -> "cba"
# "" -> ""

# inv("abc") -> inv("bc") + "a" = "cb" + "a" = "cba"
#               inv("bc") = inv("c") + "b" = "c" + "b" = "cb"
#                           inv("c") = inv("") + "c"
#                           inv("")
#                            ""



# inv(s) = s якщо s - порожній
# inv(s) = inv(s без першого симола) + перший сивол

def inv(s):
    if len(s) == 0:
        return s
    else:
        return inv(s[1:]) + s[0]

print(inv("abc"))
