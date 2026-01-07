RATES = {'RUB': 2.98, 'ARS': 0.82, 'HNL': 0.17, 'AUD': 1.9622, 'MAD': 0.208}

conicoins = float(input())
for symbol, rate in RATES.items():
    print(
        f'I will get {round(conicoins * rate, 2)} {symbol} from the sale of {conicoins} conicoins.'
    )
