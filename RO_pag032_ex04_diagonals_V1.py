#P11_diagonals_V1.py
'''Dadas las dimensiones de un bloque rectangular, calcule las diagonales de las tres
caras diferentes. Muestre el valor de la mayor '''
from math import sqrt

#Definir els valors de les variables
x = float(input("Posi l'amplada en m: "))
y = float(input("Posi la longitud en m: "))
z = float(input("Posi la proofunditat en m: "))

#Calcular les tres diagonals
primera_diagonal = sqrt(pow(x,2)+pow(y,2))
segona_diagonal = sqrt(pow(x,2)+pow(z,2))
tercera_diagonal = sqrt(pow(y,2)+pow(z,2))

# Trobar la diagonal més gran
if (primera_diagonal > (segona_diagonal and tercera_diagonal)):
    print(f"La diagonal més gran és la que les cares estan fetes per l'amplada i la longitud ({round (primera_diagonal, 2)}) m")
if (segona_diagonal > (primera_diagonal and tercera_diagonal)):
    print(f"La diagonal més gran és la que les cares estan fetes per l'amplada i la profunditat ({round (segona_diagonal, 2)}) m")
if (tercera_diagonal > (primera_diagonal and segona_diagonal )):
    print(f"La diagonal més gran és la que les cares estan fetes per la longitud i la profunditat ({round (tercera_diagonal, 2)}) m")
