from random import randrange
#import tah_s_ValueError #funkce je v předešlém úkolu
import util

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
        return util.tah(pole,i,symbol)
      
#print(tah_pocitace('-ox-x----oxxox-xxo--', 'x'))