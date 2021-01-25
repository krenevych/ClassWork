def sumaElemInFile(file_name):
    suma = 0
    with open(file_name, "r") as f:
        for line in f:
            l1 = [float(el) for el in line.split()]
            for d in l1:
                suma += d
            # l1 = line.strip()
            # print(l1)
    return suma

def MaxNum(file_name):
    l1 = []
    with open(file_name, "r") as f:
        for line in f:
            l1 += [float(el) for el in line.split()]

    return max(l1)

def VidElem(file_name):
    count = 0
    with open(file_name, "r") as f:
        for line in f:
            l1 = [float(el) for el in line.split()]
            for d in l1:
                if d < 0:
                    count += 1
    return count


def OstElem(file_name):
    with open(file_name, "r") as f:
        for line in f:
            l1 = [float(el) for el in line.split()]
            a = l1[-1]
    return a


def MaxElem(file_name):
    max = 0
    with open(file_name, "r") as f:
        for line in f:
            l1 = [float(el) for el in line.split()]
            for d in l1:
                if max < d:
                    max = d
    return max

if __name__ == "__main__":
    print(MaxElem("t2.txt"))
