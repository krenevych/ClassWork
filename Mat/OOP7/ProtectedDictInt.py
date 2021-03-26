from random import randint

from Mat.OOP7.ProtectedDictIntError import ProtectedDictIntError


class ProtectedDictInt:
    def __init__(self):
        self.dict = {}

    def __str__(self):
        return str(self.dict)

    def __setitem__(self, key, value):
        if key in self:
            raise ProtectedDictIntError(ProtectedDictIntError.KEY_EXIST, key)
        if not isinstance(key, int):
            raise ProtectedDictIntError(ProtectedDictIntError.KEY_NOT_INT, key)
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

    def __iter__(self):
        # return MyIterator(self.dict)
        return iter(self.dict)


class MyIterator:
    def __init__(self, collection: dict):
        self.sorted_collection = list(collection)
        self.sorted_collection.sort()
        self.current_index = 0

    def __next__(self):
        try:
            current = self.sorted_collection[self.current_index]
            self.current_index += 1
            return current
        except IndexError:
            raise StopIteration


if __name__ == "__main__":
    d = ProtectedDictInt()
    try:
        d[23] = 32
    except ProtectedDictIntError as e:
        print(e)

    try:
        d["23"] = 32
    except ProtectedDictIntError as e:
        print(e)

    try:
        d[23] = 32
    except ProtectedDictIntError as e:
        print(e)


    try:
        d[111] = 32
    except ProtectedDictIntError as e:
        print(e)


