wallet = {1: 2, 4: 10, 5: 5, 100: 1}

max_nom = 1000

cash = 0
for nom in range(1, max_nom + 1):
    try:
        quant = wallet[nom]
        cash += nom * quant
    except KeyError:
        pass

print(cash)
