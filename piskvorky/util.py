

def tah(pole, pozice, symbol):
    # """Vrátí herní pole s daným symbolem umístěným na danou pozici
    if pozice not in range(0,20):
        raise ValueError
    if pole[pozice] != '-':
        raise ValueError
    if symbol != 'x' and symbol != 'o':
        raise ValueError
    else:
        zacatek = pole[:pozice]
        konec = pole[pozice + 1:]
        pole_se_symbolem = zacatek + symbol + konec
        return pole_se_symbolem
      