"""
Dnešním úkolem je naprogramovat hru 1D Piškvorky. Nakonec bude fungovat následovně:

1-D piškvorky se hrají na řádku s dvaceti políčky. Hráči střídavě přidávají kolečka (`o`) a křížky (`x`), třeba:
1. kolo: -------x------------
2. kolo: -------x--o---------
3. kolo: -------xx-o---------
4. kolo: -------xxoo---------
5. kolo: ------xxxoo---------
Hráč, která dá tři své symboly vedle sebe, vyhrál.
Hru budeš skládat postupně z malých částí. Napřed tedy musíš vytvořit malé části; ty pak poskládáš dohromady.

Úkoly dělej postupně.

Odevzdávej prosím celé soubory se všemi potřebnými importy a pomocnými funkcemi.

1.
Napiš funkci vyhodnot, která dostane řetězec s herním polem 1-D piškvorek a vrátí jednoznakový řetězec podle stavu hry:

"x" – Vyhrál hráč s křížky (pole obsahuje "xxx")
"o" – Vyhrál hráč s kolečky (pole obsahuje "ooo")
"!" – Remíza (pole neobsahuje "-", a nikdo nevyhrál)
"-" – Ani jedna ze situací výše (t.j. hra ještě neskončila)
Například:

vyhodnot('--------------------') vrátí '-'
vyhodnot('--o--xxx---o--o-----') vrátí 'x'
vyhodnot('xoxoxoxoxoxoxoxoxoxo') vrátí '!'
s"""
#pole = '--------------------'

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

#vyhodnot('xxooxoxxoxooxxoxxoxx')
#vyhodnot('xx--x-x-ox---oxxoxxo')
