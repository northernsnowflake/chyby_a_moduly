"""
Napiš funkci tah_pocitace(pole, symbol), která dostane řetězec s herním polem a symbol, vybere pozici, na kterou hrát, a vrátí herní pole se zaznamenaným tahem počítače.

Použij jednoduchou náhodnou „strategii”:

Vyber číslo od 0 do 19.
Pokud je dané políčko volné, hrej na něj.
Pokud ne, opakuj od bodu 1.
Hlavička funkce by tedy měla vypadat nějak takhle:

def tah_pocitace(pole, symbol):
    Vrátí herní pole se zaznamenaným tahem počítače

    `pole` je herní pole, na které se hraje.
    `symbol` může být 'x' nebo 'o', podle toho jestli hráč hraje za křížky
    nebo za kolečka.
    
    ...
Zavolání print(tah_pocitace('o-------------------', 'x')) by mohlo vypsat třeba o---------x---------.

"""

from random import randrange
import tah_s_ValueError #funkce je v předešlém úkolu


def tah_pocitace(pole,symbol):
    """Vrátí herní pole se zaznamenaným tahem počítače

    `pole` je herní pole, na které se hraje.
    `symbol` může být 'x' nebo 'o', podle toho jestli hráč hraje za křížky
    nebo za kolečka.
    """
    while True:
        if '-' not in pole:
            raise ValueError("Všechny pozice v poli jsou obsazené")
        i = randrange(0,20)
        while pole[i] != '-':
            i = randrange(0,20)
        return tah_s_ValueError.tah(pole,i,symbol)
      
#print(tah_pocitace('-ox-x----oxxox-xxo--', 'x'))

