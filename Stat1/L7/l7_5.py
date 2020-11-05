
# 1 2 4 8 16 32 64...
# 1 0 0 1 0 = 1 * 16 + 0 * 8 +
#                   0 * 4 + 1 * 2 + 0 * 1 =
#                   = 18
def to_dec(n):
    dec = 0
    pow2 = 1
    while n > 0:
        dec += n % 10 * pow2
        pow2 *= 2
        n //= 10
    return dec

# 1 2 4 8 16 32 64...
# 0
# 10010

# 18 / 2 = 9 (0)
#          9 / 2 = 4 (1)
#                  4 / 2 = 2 (0)
#                          2 / 2 = 1 (0)
#                                  1 / 2 = 0 (1)

def to_bin(n):
    dec = 0
    pow2 = 1
    while n > 0:
        dec += n % 2 * pow2
        pow2 *= 10
        n //= 2
    return dec

A = int(input())
B = int(input())

A_dec = to_dec(A)
B_dec = to_dec(B)
A_plus_B = A_dec + B_dec
print(to_bin(A_plus_B))
