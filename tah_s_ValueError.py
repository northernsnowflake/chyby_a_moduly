
"""
Napiš funkci tah, která dostane řetězec s herním polem, číslo políčka (0-19), a symbol (x nebo o), a vrátí herní pole (t.j. řetězec) s daným symbolem umístěným na danou pozici.

Hlavička funkce by tedy měla vypadat nějak takhle:

def tah(pole, pozice, symbol):
    Vrátí herní pole s daným symbolem umístěným na danou pozici

    `pole` je herní pole, na které se hraje.
    `pozice` je číslo políčka. Čísluje se od nuly.
    `symbol` může být 'x' nebo 'o', podle toho jestli je tah za křížky
    nebo za kolečka.
    
    ...
Například:

tah('--------------------', 0, 'x') vrátí 'x-------------------'
tah('--------------------', 19, 'o') vrátí '-------------------o'
tah('x-o-x-o-x-o-x-o-x-o-', 5, 'x') vrátí 'x-o-xxo-x-o-x-o-x-o-'
Můžeš využít nějakou funkci, kterou už máš napsanou?
----------
Přepiš funkci tah, aby skončila s chybou ValueError v těchto případech:

Hra na pozici, která není v poli, např. tah('--------------------', -1, 'x')

Hra na obsazené políčko, např. tah('x-------------------', 0, 'o')

Hra jiným symbolem než 'x' nebo 'o', např. tah('--------------------', 0, 'řeřicha')


"""


# už to vrací správně Hra jiným symbolem než 'x' nebo 'o', např. tah('--------------------', 0, 'řeřicha')
# Hra na pozici, která není v poli, např. tah('--------------------', -1, 'x')
# Hra na obsazené políčko, např. tah('x-------------------', 0, 'o')

def tah(pole, pozice, symbol):
    # """Vrátí herní pole s daným symbolem umístěným na danou pozici
    if pozice not in range(0,20):
        #print("funkce tah, mimo range 0,20")
        raise ValueError
    if pole[pozice] != '-':
        #print("funkce tah, pozice je obsazena")
        raise ValueError
    if "x" != symbol and "o" != symbol:
        #print("funkce tah, neni x ani o")
        raise ValueError
    else:
        zacatek = pole[:pozice]
        konec = pole[pozice + 1:]
        pole_se_symbolem = zacatek + symbol + konec
        return pole_se_symbolem

#print(tah('--------------------', -1, 'x'))
#print(tah('x-------------------', 0, 'o'))
#print(tah('--------------------', 0, 'řeřicha'))