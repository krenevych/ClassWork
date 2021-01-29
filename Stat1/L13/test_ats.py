L = open("t2.txt")
k = L.read()
L.close()

print(k)
S = k.split()
print(S)
m = 0
for i in S:
    m += float(i)
print(m)
