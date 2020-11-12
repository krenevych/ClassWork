
#  "asd" -> "dsa"

# 'a' '' стоп, нічого робити не треба
# "asd" ->  inv("sd")   + 'a'

# inv(s) = s, якщо s порожній
# inv(s) = inv(s без першої літери) + перша літера слова s

# inv("asd") = "ds" + 'a' = 'dsa'
#              'd' + 's' = "ds"
#                "" + 'd' = 'd'
#                   ""

def inv(s):
    if len(s) == 0:
        return s
    else:
        return inv(s[1:]) + s[0]

print(inv("hello!"))




