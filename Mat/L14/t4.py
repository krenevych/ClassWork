# file_name = str(input())
file_name = "D:/Repo/my_files/test.txt"

try:
    with open(file_name, "r") as f:
        for line in f:
            print(line)
except FileNotFoundError:
    print("File not found!")
except IOError:
    print("File not found!")

