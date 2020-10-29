
s = input()
s = s[1:] if s[0] == '+' or s[0] == '-' else s

print(s.count('+') + s.count('-') + s.count('*'))