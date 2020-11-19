s = input()
freq = {el: s.count(el) for el in s}

max_char = max(freq)

print(max_char, freq[max_char])