
def showFile(filename):
    with open(filename) as f:
        for line in f:
            print(line, end="")

try:
    showFile("t22.py")
except FileNotFoundError as e:
    print(e)