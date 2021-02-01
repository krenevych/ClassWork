wallet = {2: 4, 100: 1, 5: 3}
max_nom = 1000

capital = 0
for nom in range(1, max_nom + 1):
    try:
        capital += nom * wallet[nom]
    except KeyError:
        pass
#
# for nom in wallet:
#     capital += nom * wallet[nom]

print(capital)
# print(wallet[15])