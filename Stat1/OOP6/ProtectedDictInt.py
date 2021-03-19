from random import randint


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

    def __iter__(self):
        return iter(self.dict)
        # return MyDictIterator(self.dict) # - екземпляр класу Ітератор

# користувацький клас Ітератор, для ітерування екземплярів
# класу ProtectedDictInt
class MyDictIterator:
    def __init__(self, collection):
        self.collection_sorted = list(collection)
        self.collection_sorted.sort()
        self.current = 0

    def __next__(self):
        # опишемо як ітератор має проходити колекцію

        if self.current >= len(self.collection_sorted):
            raise StopIteration

        res  = self.collection_sorted[self.current]
        self.current += 1
        return res




if __name__ == "__main__":
    d = ProtectedDictInt()
    d[23] = 32
    d[232] = 232
    d[333] = 333
    d[111] = 111

    for i in range(20):
        try:
            key = randint(0, 1000)
            d[key] = key
        except:
            pass

    # print(d)
    # print("=====================")

    # it = iter(d)
    #
    # try:
    #     el = next(it)
    #     print(el)
    # except StopIteration:
    #     pass
    #
    # try:
    #     el = next(it)
    #     print(el)
    # except StopIteration:
    #     pass
    #
    # try:
    #     el = next(it)
    #     print(el)
    # except StopIteration:
    #     pass

    for key in d:
        print(key)

    # d_ordinary = {}
    # d_ordinary[23] = 32
    # d_ordinary[232] = 232
    # d_ordinary[333] = 333
    # d_ordinary[111] = 111
    # for key in d_ordinary:
    #     print(key)