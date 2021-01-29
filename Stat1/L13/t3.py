
def createFile9(filename):
    with open(filename, "w") as f:
        for i in range(1, 10):
            print(str(i) * i, file=f)


createFile9("t3.txt")