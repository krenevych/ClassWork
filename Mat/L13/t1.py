def showFile(file_name):
    f = open(file_name, "r")
    for line in f:
        l1 = line.strip()
        print(l1)
    f.close()


def showFile60(file_name):
    f = open(file_name, "r")
    for line in f:
        l1 = line.strip()
        if len(l1) > 60:
            print(l1)
    f.close()


def countEmpty(file_name):
    counter = 0
    f = open(file_name, "r")
    for line in f:
        l1 = line.strip()
        if len(l1) == 0:
            counter += 1
    f.close()
    return counter


def findMaxStr(file_name):
    maxStr = ""
    f = open(file_name, "r")
    for line in f:
        l1 = line.strip()
        if len(maxStr) < len(l1):
            maxStr = l1
    f.close()
    return maxStr


###########################################
if __name__ == "__main__":
    # showFile60("t1.txt")
    # counter = countEmpty("t11.txt")
    # print(counter)
    maxStr = findMaxStr("t11.txt")
    print(maxStr)



