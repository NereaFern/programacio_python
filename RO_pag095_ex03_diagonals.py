#R0_Pag_95_ex_3_diagonals.py
'''3. Dadas las dimensiones de un bloque rectangular, calcule las diagonales de las tres
caras diferentes. Muestre el valor de la mayor diagonal.'''
from math import*

altura=float(input("Posi el valor de l'altura: "))
base=float(input("Posi el valor de la base: "))
profunditat=float(input("Posi el valor de la profunditat :"))

diagonal1=sqrt(pow(base,2)+pow(altura,2))
diagonal2=sqrt(pow(base,2)+pow(profunditat,2))
diagonal3=sqrt(pow(altura,2)+pow(profunditat,2))

if(diagonal1==diagonal2 or diagonal2==diagonal3):
    print("Totes les diagonals tenen el mateix valor:", diagonal1)
elif(diagonal1==diagonal2):
    if(diagonal1>diagonal3):
        print("Les diagonals més grans son la 1 i la 2:", diagonal1)
    else:
        print("La diagonal més gran és la 3:", diagonal3)
elif(diagonal1==diagonal3):
    if(diagonal1>diagonal2):
        print("Les diagonals més grans son la 1 i la 3:", diagonal1)
    else:
        print("La diagonal més gran és la 2:", diagonal2)
elif(diagonal2==diagonal3):
    if(diagonal2>diagonal1):
        print("Les diagonals més grans son la 2 i 3:", diagonal2)
    else:
        print("La diagonal més gran és la 1:", diagonal1)
elif(diagonal1>diagonal2 and diagonal1>3):
    print("La diagonal més gran és la 1:", diagonal1)
elif(diagonal2>diagonal3 and diagonal2>diagonal1):
    print("La diagonal més gran és la 2:", diagonal2)
else:
    print("La diagonal més gran és la 3:", diagonal3)