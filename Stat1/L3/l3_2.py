
# n = 17
# 2 4 8 16

n = int(input())
res = 2  # 2^1

while res < n:
    print(res, end=" ")
    # print(res, end="***")
    # print(res)
    res *= 2


