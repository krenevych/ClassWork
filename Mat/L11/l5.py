
#  0, 1, 1, 2, 4, 7, 13...
#  T3 T2 T1 T
#     T3 T2 T1
# 0, 1, 2, 3, 4, 5, 6,
N = int(input("N= "))

T3 = 0
T2 = 1
T1 = 1
for k in range(3, N+1):
    # T = T1 + T2 + T3
    # T3 = T2
    # T2 = T1
    # T1 = T
    T1, T2, T3 = T1 + T2 + T3, T1, T2

print(T1)

# 5:   7
# 10:   149
# 31:   53798080
