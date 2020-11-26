# 0   1   2   3   4   5    6    7
# 0   1   1   2   4   7   13   24
# T3 T2  T1   T
#    T3  T2  T1


N = int(input("N= "))

T3 = 0
T2 = 1
T1 = 1
for n in range(3, N + 1):
    T3, T2, T1 = T2, T1, T1 + T2 + T3

    print(T1)

