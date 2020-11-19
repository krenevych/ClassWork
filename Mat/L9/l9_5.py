
S = input()

freq = {elem: S.count(elem) for elem in S}
# print(freq)

max_char = max(freq)

print(max_char, freq[max_char])

