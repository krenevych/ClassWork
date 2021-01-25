

def constructFile1_9(file_name):
    f = open(file_name, "w")

    for i in range(1, 10):
        print(str(i) * i)
        print(str(i) * i, file=f)

    f.close()

def constructFile1_9_manager_context(file_name):
    with open(file_name, "w") as f:  #    f = open(file_name, "w")
        for i in range(1, 10):
            print(str(i) * i, file=f)
    # не потрібно закривати файл,
    # бо менеджер контексту with зробить це за нас самостійно

if __name__ == "__main__":
    constructFile1_9_manager_context("t31.txt")