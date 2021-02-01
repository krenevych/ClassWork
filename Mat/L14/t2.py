s = "asd456f6;la8sk3d4444jf;2la3sjdf"

res = 0
for c in s:
    try:
        res += int(c)
    except ValueError:
        pass

print(res)