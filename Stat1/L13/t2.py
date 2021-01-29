def file_count(filename):
    k = 0
    with open(filename) as f:
        for line in f:
            f_list = line.split()
            # print(f_list)
            for i in f_list:
                if float(i) < 0:
                    k += 1
            # print(line)
    return k


print(file_count("t2.txt"))
