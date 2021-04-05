
def range(start, end, step=1):
    current = start
    while current < end:
        yield current
        current += step


for i in range(2, 10):
    print(i)