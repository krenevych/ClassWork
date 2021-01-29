def f_b(lines:list):
    result = []

    for line in lines:
        s = line.strip()
        if len(s) > 60:
            result.append(s)

    return result

def f_c(lines:list):
    return [lines.count('')]

def f_d(lines:list):
    max_len = -1
    for line in lines:
        s = line.strip()
        s_len = len(s)
        if s_len > max_len:
            max_len = s_len
    return [0 if max_len == -1 else max_len]


def print_file(filename, func):
    with open(filename) as f:
        lines = f.readlines()
    return func(lines)

lst = print_file('t.txt', f_c)
print(lst)