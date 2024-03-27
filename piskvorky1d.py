"""
Napiš funkci piskvorky1d, která:

Vytvoří řetězec s herním polem, '--------------------'
Stále dokola:
zavolá volá funkci tah_hrace, a výsledek uloží jako nové pole
vypíše herní pole
zavolá volá funkci tah_pocitace, a výsledek uloží jako nové pole
vypíše herní pole
Zatím neřeš konec hry.

----
Teď pošéfuj konec hry. Když někdo vyhraje nebo dojde k remíze, cyklus se ukončí a vypíše se výsledek – třeba s gratulací nebo povzbuzující zprávou.

Stav hry kontroluj po každém tahu.

Nezapomeň, že máš k dispozici funkci vyhodnot!
"""
import tah_hrace
import tah_pocitace
import vyhodnot

#pole = '--------------------'

def piskvorky1d():
    pole = '--------------------'
    while '-' in pole:
        pole = tah_hrace.tah_hrace(pole,'o')
        print(pole)
        hodnoceni = vyhodnot.vyhodnot(pole)
        if hodnoceni == 'x':
            print("Gratuluji, hráči s křížky!")
            break
        if hodnoceni == 'o':
            print("Gratuluji, hráči s kolečky!")
            break
        if hodnoceni == '!':
            print("Díky za hru")
            break
        pole = tah_pocitace.tah_pocitace(pole,'x')
        print(pole)
        hodnoceni = vyhodnot.vyhodnot(pole)
        if hodnoceni == 'x':
            print("Gratuluji, hráči s křížky!")
            break
        if hodnoceni == 'o':
            print("Gratuluji, hráči s kolečky!")
            break
        if hodnoceni == '!':
            print("Díky za hru")
            break

print(piskvorky1d())