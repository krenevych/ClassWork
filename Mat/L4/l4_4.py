counter = 0

while True:
    i = int(input())
    if i == 0:
        break

    if i % 2 == 0:
        continue

    counter += 1

print(counter)