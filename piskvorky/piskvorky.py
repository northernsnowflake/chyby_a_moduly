"""Program rozděl do modulů a uprav importy tak, aby program stále fungoval. Moduly by neměly mít vedlejší efekty.

Funkce vyhodnot, tah_hrace a piskvorky1d patří do modulu piskvorky (tj. souboru piskvorky.py).
Funkce tah_pocitace patří do modulu ai (tj. souboru ai.py).
Funkci tah zařaď podle materiálů o cyklických importech.
Protože samotná hra – vypisování a ptaní na otázky – je vedlejší efekt, tak teď nepůjde spustit. Aby to šlo, vytvoř ještě „spouštěcí“ modul hra (tj. soubor hra.py) s následujícím obsahem:

from piskvorky import piskvorky1d

piskvorky1d()
Odevzdávání a kontrola několika souborů je zatím složité, proto si tento úkol zkontroluj sama:

Všechny funkce jsou kde mají být (podle zadání).
Příkaz python hra.py v příkazové řádce spustí funkční hru.
Příkaz import piskvorky v Pythonu nespustí hru (a nemá ani další vedlejší efekty).
"""
import ai
import util


def vyhodnot(pole):
    # Vyhrál hráč s křížky
    if "xxx" in pole:
        #print('vyhrál hráč s křížky')
        return "x"
    # Vyhrál hráč s kolečky
    if "ooo" in pole:
        #print('vyhrál hráč s kolečky')
        return "o"
    if "-" not in pole:
        #print('remíza')
        return "!"
    else:
        #print('hra ještě neskončila')
        return '-'



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
            pole_s_tahem_hrace = util.tah(pole,pozice,symbol)
            return pole_s_tahem_hrace
        except ValueError:
            print('Tam nejde hrát ')



#pole = '--------------------'

def piskvorky1d():
    pole = '--------------------'
    while '-' in pole:
        pole = tah_hrace(pole,'o')
        print(pole)
        hodnoceni = vyhodnot(pole)
        if hodnoceni == 'x':
            print("Gratuluji, hráči s křížky!")
            break
        if hodnoceni == 'o':
            print("Gratuluji, hráči s kolečky!")
            break
        if hodnoceni == '!':
            print("Díky za hru")
            break
        pole = ai.tah_pocitace(pole,'x')
        print(pole)
        hodnoceni = vyhodnot(pole)
        if hodnoceni == 'x':
            print("Gratuluji, hráči s křížky!")
            break
        if hodnoceni == 'o':
            print("Gratuluji, hráči s kolečky!")
            break
        if hodnoceni == '!':
            print("Díky za hru")
            break

#print(piskvorky1d())