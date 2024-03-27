"""
Napiš funkci tah_hrace(pole, symbol), která dostane řetězec s herním polem a symbol (x nebo o) a:

zeptá se hráče, na kterou pozici chce hrát,
pomocí funkce tah zjistí, jak vypadá herní pole se zaznamenaným tahem hráče
vrátí toto herní pole se zaznamenaným tahem hráče.
Pokud uživatel zadá špatný vstup (nečíslo, záporné číslo, obsazené políčko apod.), funkce mu vynadá a zeptá se znova. (Není potřeba použít pro každý případ jinou hlášku.)

Hlavička funkce by tedy měla vypadat nějak takhle:

def tah_hrace(pole, symbol):
    Zeptá se hráče na tah a vrátí nové herní pole

    `pole` je herní pole, na které se hraje.
    `symbol` může být 'x' nebo 'o', podle toho jestli hráč hraje za křížky
    nebo za kolečka.
    
    ...
Například zavolání print("Nový stav hry je:", tah_hrace('o-------------------', 'x')) by mohlo dopadnout takto:

Kam chceš hrát? nevím
Zadávej čísla!
Kam chceš hrát? 0
Tam nejde hrát!
Kam chceš hrát? -1
Tam nejde hrát!
Kam chceš hrát? 151
Tam nejde hrát!
Kam chceš hrát? 2
Nový stav hry je: o-x-----------------
"""
import tah_s_ValueError

def tah_hrace(pole, symbol):
    #"""Zeptá se hráče na tah a vrátí nové herní pole
    #`pole` je herní pole, na které se hraje.
    #`symbol` může být 'x' nebo 'o', podle toho jestli hráč hraje za křížky
    #nebo za kolečka.
    #"""
    while True:
        pozice = input('Kam chceš hrát? ')
        try:
            pozice = int(pozice)
        except ValueError:
            print('Zadávej čísla')
            continue
        try:
            pole_s_tahem_hrace = tah_s_ValueError.tah(pole,pozice,symbol)
            return pole_s_tahem_hrace
        except ValueError:
            print('Tam nejde hrát ')
            
#print("Nový stav hry je:", tah_hrace('o-------------------', 'x'))