
class ProtectedDictInt:
    def __init__(self):
        self.dict = {}

    def __str__(self):
        return str(self.dict)

    def __setitem__(self, key, value):
        if key in self:
            raise RuntimeError
        if not isinstance(key, int):
            raise RuntimeError
        self.dict[key] = value

    def __getitem__(self, item):
        return self.dict[item]

    def __contains__(self, item):
        return item in self.dict

    def __len__(self):
        return len(self.dict)

    def __add__(self, other):
        result = ProtectedDictInt()
        for key, val in self.dict.items():
            result[key] = val

        if isinstance(other, tuple) and len(other) == 2:
            result[other[0]] = other[1]
        elif isinstance(other, ProtectedDictInt):
            for key, val in other.dict.items():
                result[key] = val

        return result

    def __sub__(self, other):
        if not isinstance(other, int):
            raise RuntimeError

        result = ProtectedDictInt()
        for key, val in self.dict.items():
            if key == other:
                continue
            result[key] = val

        return result


if __name__ == "__main__":
    d = ProtectedDictInt()
    d[23] = 32
    d[23] = 132
    d[232] = 232
    d[333] = 333
    print(d)

    d2 = d + (2, 3)

    d1 = ProtectedDictInt()
    d1[123] = 14
    d = d + d1

    # d3 = d - (23, 23)
    d3 = d - 23
    pass