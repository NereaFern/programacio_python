#RO_Pag_121.1_exemple_granota.py
'''Escribir un programa para simular el siguiente juego: Una rana es colocada en
la casilla central de una caja cuadriculada de tamaño 9x9 dm. La rana realiza saltos
aleatoriamente de 1 dm. en cualquiera de las cuatro direcciones: arriba, abajo, izquierda o
derecha. Determine la cantidad de saltos realizados hasta llegar a alguno de los bordes de
la caja.'''
from random import*
#initzialitzem variables
x=0#moviment horitzontal
y=0#moviment vertical
i=0 #Comptador
#aquí el que fem és veure quan la granota arribarà a la última casella
while x!=4 and x!=-4 and y!=4 and y!=-4:
    numero=randint(1,4)#número que surt en el dau
    if numero==1:
        x+=1
    elif numero==2:
        x-=1
    elif numero==3:
        y+=1
    elif numero==4:
        y-=1
    i+=1
print(x)
print(y)
print(i)
