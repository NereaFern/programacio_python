'''
4. Dadas las dimensiones de un bloque rectangular, calcule las diagonales
de las tres caras diferentes. Muestre el valor de la mayor diagonal. '''

from math import sqrt

#Variables
costat_a = float(input("Introdueix el costat a del bloc rectangular: "))
costat_b = float(input("Introdueix el costat b del bloc rectangular: "))
costat_c = float(input("Introdueix el costat c del bloc rectangular: "))
          
# Càlculs
diagonal_ab = sqrt(pow(costat_a,2)+pow(costat_b,2))
diagonal_ac = sqrt(pow(costat_a,2)+pow(costat_c,2))
diagonal_bc = sqrt(pow(costat_b,2)+pow(costat_c,2))

# Trobem la diagonal major
if (diagonal_ab > diagonal_ac):
    if (diagonal_ab > diagonal_bc):
        print(f"La diagonal major es la de la cara ab i val {round(diagonal_ab, 2)}")
    else:
        print(f"La diagonal major es la de la cara bc i val {round(diagonal_bc, 2)}")
else:
    if (diagonal_ac > diagonal_bc):
        print(f"La diagonal major es la de la cara ac i val {round(diagonal_ac, 2)}")
    else:
        print(f"La diagonal major es la de la cara bc i val {round(diagonal_bc, 2)}")

print("FI DE PROGRAMA")
        
                 
                 
                 