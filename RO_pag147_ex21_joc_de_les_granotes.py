#RO_Pag_147_ex_21_joc_de_les_granotes.py
'''Escriba un programa para simular el siguiente juego: Una rana es colocada en el
centro de un camino de 20 mt. La rana realiza saltos aleatoriamente de 1 mt. en
cualquiera de las dos direcciones: izquierda o derecha. Determine la cantidad de saltos
realizados hasta llegar a alguno de los dos extremos.'''
from random import choice
#Initzialitzem les variables:
x=10
llista=[1,-1]
i=0#Comptador
while x!=20 and x!=0:
    n=choice(llista)
    x+=n
    i+=1
print(f"La quantitat de salts que ha hagut de fer fins arribar a un dels extrems son {i}")