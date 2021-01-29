def showFile(filename, func):
    with open(filename) as f:  # f = open(filename)
        for line in f:
            s = line.strip()
            if func(s):
                print()


try:
    showFile("t1.txt", lambda x: x > 60)
except:
    pass