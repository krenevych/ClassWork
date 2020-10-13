n = int(input())

# n = 123
# count = 0

count = 0 if n > 0 else 1

while n > 0:
    count = count + 1
    n = n // 10

print(count)
