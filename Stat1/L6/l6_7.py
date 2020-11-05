
words = []
while True:
    try:
        s = input()
        words = words + s.split()
    except:
        break

for word in words:
    print(len(word), end=" ")

